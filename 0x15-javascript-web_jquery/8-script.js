const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  $.each(data.results, function (i, results) {
    $('UL#list_movies').append('<li>' + results.title + '</li>');
  });
});
