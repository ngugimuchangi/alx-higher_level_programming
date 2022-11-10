#!/usr/bin/node
/* Rectangle class
 * Properties: width, height
 * Methods: print, rotate, double
 */
class Rectangle {
  // constructor method
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // print method
  print () {
    for (let h = this.height; h > 0; h--) {
      let str = '';
      for (let w = this.width; w > 0; w--) {
        str += 'X';
      }
      console.log(str);
    }
  }

  // rotate method
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // area method
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
