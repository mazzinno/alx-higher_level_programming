#!/usr/bin/node
const FS = require('fs');
const FILE_PATH = process.argv[2];

FS.readFile(FILE_PATH, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
