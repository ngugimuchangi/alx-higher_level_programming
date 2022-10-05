#!/usr/bin/node

// Script to join and print CLI arguments

const args = process.argv.slice(2);
const len = args.length;

if (len === 0) {
  console.log('undefined is undefined');
} else if (len === 1) {
  console.log(`${args[0]} is undefined`);
} else {
  console.log(`${args[0]} is ${args[1]}`);
}
