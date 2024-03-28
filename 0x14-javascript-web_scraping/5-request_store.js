#!/usr/bin/node
const link = process.argv[2];
const PATH = process.argv[3];
const REQUEST = require('request');
const FS = require('fs');

REQUEST(link, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    FS.writeFile(PATH, body, 'utf8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
