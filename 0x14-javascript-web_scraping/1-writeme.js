#!/usr/bin/node
// Function that writes a string to a file

const writeFile = require('fs').writeFile;
const filename = process.argv[2];
const data = process.argv[3];

writeFile(filename, data, 'utf8', (error) => {
  if (error) throw error;
});
