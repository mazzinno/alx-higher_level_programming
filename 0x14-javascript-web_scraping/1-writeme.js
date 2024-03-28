#!/usr/bin/node
const FS = require('fs');
const FILE_PATH = process.argv[2];
const STR = process.argv[3];
FS.writeFile(FILE_PATH, STR, 'utf8', function (err) {
  if (err) {
    console.error(err);
  }
});
