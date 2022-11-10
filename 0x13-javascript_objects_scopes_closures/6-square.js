#!/usr/bin/node
/*
 * Square class definition
 * Attributes: size
 * Methods: charPrint
 * Inherits from 5-square.js
 */
const Parent = require('./5-square');

class Square extends Parent {
  // print method
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let h = this.height; h > 0; h--) {
        let str = '';
        for (let w = this.width; w > 0; w--) {
          str += c;
        }
        console.log(str);
      }
    }
  }
}
module.exports = Square;
