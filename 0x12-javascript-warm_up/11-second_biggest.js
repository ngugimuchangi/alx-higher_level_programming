#!/usr/bin/node

// Script to search the second biggest integer in a list of arguments

const args = process.argv.splice(2);
const len = args.length;

if (len === 0 || len === 1) {
  console.log(0);
} else {
  const intArgs = args.map(arg => { return parseInt(arg); });
  const largest = Math.max(...intArgs);
  const numIndex = intArgs.indexOf(largest);
  intArgs.splice(numIndex, 1);
  const secondLargest = Math.max(...intArgs);
  console.log(secondLargest);
}
