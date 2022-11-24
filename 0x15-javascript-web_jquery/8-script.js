// Makes ajax call to swapi-api
$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: (data) => {
      $.each(data.results, (index, movie) => {
        $('ul#list_movies').append($('<li></li>').text(movie.title));
      });
    }
  });
});
