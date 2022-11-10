#!/usr/bin/node
/*
 * Script that import an array and computes a new array
 * New list must be created with each value equal to the
 * value of the initial list multiplied by the index in
 * the list
 */
const list = require('./100-data').list;

console.log(list);
const newList = list.map((element, index) => element * index);
console.log(newList);
