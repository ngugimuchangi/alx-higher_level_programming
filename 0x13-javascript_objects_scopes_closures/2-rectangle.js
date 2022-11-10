#!/usr/bin/node
/* Rectangle class defintion
 * Properties: width and height
 */
class Rectangle {
  // constructor method
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
