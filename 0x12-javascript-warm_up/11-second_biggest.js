#!/usr/bin/node

// Script to search the second biggest integer in a list of arguments

let args = process.argv.splice(2);
len = args.length;

if (len === 0 || len === 1)
{
  console.log(0);
}
else {
  intArgs = args.map(arg => {return parseInt(arg);});
  let largest = intArgs[0];
  for (let items of intArgs)
}
