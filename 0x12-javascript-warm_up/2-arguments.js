#!/usr/bin/node
const manyArgs = process.argv.length - 2;
if (manyArgs === 0) {
  console.log('No argument');
} else if (manyArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
