from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from listings.models import Books
from listings.serializers import UserSerializer, BooksSerializer
from rest_framework.authtoken.models import Token
from rest_framework import viewsets

from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework import pagination
from rest_framework import filters
import django_filters


# Create your views here.


def index(request):
    return render(request, 'listings/index.html')


@api_view(['POST'])
def login(request):
    d = request.data
    s = UserSerializer(data=d)
    if s.is_valid():
        try:
            user = User.objects.get(email=d['email'])
        except User.DoesNotExist:
            user = User()
            user.first_name = d['first_name']
            user.last_name = d['last_name']
            user.email = d['email']
            user.username = d['id']
            user.set_password(d['id'] + d['email'] + 'Sarthak')
            user.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 12


class BooksFilter(filters.FilterSet):
    owner = django_filters.CharFilter(name="owner__first_name")

    class Meta:
        model = Books
        fields = ['title', 'author', 'owner']


@authentication_classes((TokenAuthentication,))
class BooksViewSet(viewsets.ModelViewSet):

    """
    Retrieve books
    """
    queryset = Books.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = BooksSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = BooksFilter
    # check pernission if user is owner then only allow user for
    # make it only read only

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
