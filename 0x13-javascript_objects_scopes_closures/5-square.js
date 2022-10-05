#!/usr/bin/node
const rec = require('./4-rectangle');
class Square extends rec {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
