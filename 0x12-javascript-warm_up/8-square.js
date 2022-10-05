#!/usr/bin/node

// Script to print a square

const args = process.argv.splice(2);
const len = args.length;

if (len === 0 || isNaN(args[0])) {
  console.log('Missing size');
} else {
  const times = parseInt(args[0]);
  if (times > 0) {
    for (let i = 0; i < times; i++) {
      let mySquare = '';
      for (let j = 0; j < times; j++) {
        mySquare += 'X';
      }
      console.log(mySquare);
    }
  }
}
