 $(document).on('click', '.filters', function() {
    var filterLabel = document.getElementById('filter-value');
     filterLabel.textContent = this.text;
  });

$(document).on('click','#submit-button',function(){
  // remove the already existing table
  $("#table tr td").remove();
  var filterValue = document.getElementById('filter-value').textContent.toLowerCase();
  var searchTerm = document.getElementById('search-bar').value;
  var searchQuery = "/books/?" + filterValue +  "=" + searchTerm;
  console.log('searchQuery',searchQuery);
  fetch(searchQuery)
    .then(function(response){
      if(response.status!==200){
        console.log("problem with response" + response.status);
        return;
      }
      response.json().then(function(data){
        if(data){
          console.log(data);
          var len = data.results.length;
          var text = "";
          if(len>0){
            for(var i=0;i<len;i++){
              if(data.results[i].title && data.results[i].author){
                text +="<tr><td>"+data.results[i].id+"</td><td>"+data.results[i].title+"</td><td>"+data.results[i].author+"</td><td>"+data.results[i].availability+"</td></tr>";
              }
            }
            if(text != ""){
              $("#table").append(text).removeClass("hidden");
            }
          }
        }
      });
    })
});
