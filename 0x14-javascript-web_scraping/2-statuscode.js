#!/usr/bin/node
const link = process.argv[2];
const REQUEST = require('request');

REQUEST.get(link, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
