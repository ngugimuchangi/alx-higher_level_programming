#!/usr/bin/node
/*
 * Script that import an array and computes a new array
 * New list must be created with each value equal to the
 * value of the initial list multiplied by the index in
 * the list
 */
let list = require('./100-data').list;

console.log(list);
list = list.map(element => element * list.indexOf(element));
console.log(list);
