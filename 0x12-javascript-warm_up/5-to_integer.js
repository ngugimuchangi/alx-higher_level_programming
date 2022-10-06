#!/usr/bin/node

// Script to convert strings into integers

const args = process.argv.slice(2);
const len = args.length;

if (len === 0 || isNaN(args[0])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(args[0])}`);
}
