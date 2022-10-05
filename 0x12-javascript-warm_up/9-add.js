#!/usr/bin/node

// Script to add two integer argument

const args = process.argv.splice(2);
const len = args.length;

if (len < 2 || isNaN(args[0]) || isNaN(args[1])) {
  console.log('NaN');
} else {
  let sum = parseInt(args[0]) + parseInt(args[1]);
  console.log(sum);
}
