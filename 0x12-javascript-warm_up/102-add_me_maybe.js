#!/usr/bin/node

// Function that increments and calls a function

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
