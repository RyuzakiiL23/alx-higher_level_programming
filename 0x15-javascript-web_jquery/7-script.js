const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json"
$.get(url, function(data){
	$(document).ready(function(){
		$("#character").text(data.name)
	});
});
