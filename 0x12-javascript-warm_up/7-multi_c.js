#!/usr/bin/node

// Script to print text for a number of occurrences

const args = process.argv.splice(2);
const len = args.length;

if (len === 0 || isNaN(args[0])) {
  console.log('Missing number of occurrences');
} else {
  const times = parseInt(args[0]);
  if (times > 0) {
    for (let i = 0; i < times; i++) {
      console.log('C is fun');
    }
  }
}
