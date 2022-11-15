#!/usr/bin/node
// Script to get the conetents of a
// webpage and store it in a file

const request = require('request');
const writeFile = require('fs').writeFile;
const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (error) throw error;
  if (response) {
    writeFile(file, body, 'utf8', (error) => {
      if (error) throw error;
    });
  }
});
