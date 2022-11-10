#!/usr/bin/node
/* Rectangle class
 * Properties: width, height
 * Methods: print
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
}
module.exports = Rectangle;
