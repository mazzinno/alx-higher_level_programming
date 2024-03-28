#!/usr/bin/node
const MOVIE_ID = process.argv[2];
const link = 'https://swapi-api.alx-tools.com/api/films/' + MOVIE_ID
const REQUEST = require('request');

REQUEST.get(link, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
