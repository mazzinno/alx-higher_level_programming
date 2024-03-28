#!/usr/bin/node
const fs = require('fs');
// The string to write to the file
const content = process.argv[3];
// Path to the file
const filePath = process.argv[2];;
// Write the string to the file asynchronously
fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) {
        console.error(err);
    }
});
