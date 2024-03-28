#!/usr/bin/node
const REQUEST = require('request');
const URL = process.argv[2];
REQUEST.get(URL, function (err, _, body) {
  let counter = 0;
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  for (let n = 0; data.results[n] !== undefined; n++) {
    if (data.results[n].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      counter++;
    }
  }
  console.log(counter);
});
