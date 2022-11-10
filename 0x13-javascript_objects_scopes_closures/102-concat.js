#!/usr/bin/node

const fs = require('fs');

const args = process.argv.slice(2);
const len = args.length;

if (len > 2) {
  let str = '';
  fs.readFile(args[0], (err, data) => {
    if (err) throw err;
    str += data;
  });
  fs.readFile(args[1], (err, data) => {
    if (err) throw err;
    str = str.concat(data);
    fs.writeFile(args[2], str, (err) => {
      if (err) throw err;
    });
  });
}
