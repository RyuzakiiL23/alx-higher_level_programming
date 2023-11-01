const url = "https://swapi-api.alx-tools.com/api/films/?format=json";

$(document).ready(function () {
  $.get(url, function (data) {
    const len = data.results.length;
    
    const $listMovies = $("ul#list_movies");

		let i = 0
    while (i < len) {
      $listMovies.append(`<li>${data.results[i].title}</li>`);
			i++;
    }
  });
});
