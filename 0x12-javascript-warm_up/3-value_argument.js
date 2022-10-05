#!/usr/bin/node

// Script to check for and print CLI arguments

const args = process.argv.slice(2);

if (args[0] === undefined) {
  console.log('No argument');
} else {
    console.log(args[0]);
}
