#!/usr/bin/node
const REQUEST = require('request');
const URL = process.argv[2];
REQUEST.get(URL, function (err, _, body) {
  let count = 0;
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  for (let i = 0; data.results[i] !== undefined; i++) {
    if (data.results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
