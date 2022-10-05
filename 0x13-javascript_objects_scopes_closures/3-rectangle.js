#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let v = 0; v < this.width; v++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}
module.exports = Rectangle;
