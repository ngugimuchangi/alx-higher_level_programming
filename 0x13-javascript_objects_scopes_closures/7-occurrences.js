#!/usr/bin/node
// function that returns the number of occurrence in a list

exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  for (const i of list) {
    if (i === searchElement) {
      occur += 1;
    }
  }
  return occur;
};
