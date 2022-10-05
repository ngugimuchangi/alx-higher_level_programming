#!/usr/bin/node

// Script to add two integer argument

// Addition function
function add (a, b) {
  const res = a + b;
  return res;
}

const args = process.argv.splice(2);
const len = args.length;

if (len < 2 || isNaN(args[0]) || isNaN(args[1])) {
  console.log('NaN');
} else {
  const sum = add(parseInt(args[0]), parseInt(args[1]));
  console.log(sum);
}
