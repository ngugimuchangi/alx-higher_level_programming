#!/usr/bin/node
/* Script to sort dictionary by values
 * New dictionary consists of the values
 * as keys and associated keys for as values
 * If the keys had the same value, they should
 * be bundled into a list
 */
const dict = require('./101-data').dict;
const newDict = {};
for (const i in dict) {
  if (newDict[dict[i]] === undefined) {
    newDict[dict[i]] = [];
  }
  newDict[dict[i]].push(i);
}
console.log(newDict);
