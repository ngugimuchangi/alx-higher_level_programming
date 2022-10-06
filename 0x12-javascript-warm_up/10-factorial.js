#!/usr/bin/node

// Script to compute the factorial of numbers

// Recursive factorial fucntion
function factorial (num) {
  if (num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const args = process.argv.slice(2);
const len = args.length;

if (len === 0 || isNaN(args[0])) {
  console.log(1);
} else {
  let num = parseInt(args[0]);
  let myFactorial;
  if (num < 0) {
    num *= -1;
    myFactorial = factorial(num);
    if (num % 2) {
      myFactorial *= -1;
    }
  } else {
    myFactorial = factorial(parseInt(args[0]));
  }
  console.log(myFactorial);
}
