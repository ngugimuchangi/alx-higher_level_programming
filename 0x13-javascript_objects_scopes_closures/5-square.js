#!/usr/bin/node
/*
 * Square class definition
 * Attributes: size
 * Inherits from 4-recatangle.js
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  // constructor method
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
