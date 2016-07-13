from django.conf.urls import url, include
from listings import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books', views.BooksViewSet)

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^', include(router.urls))
]

