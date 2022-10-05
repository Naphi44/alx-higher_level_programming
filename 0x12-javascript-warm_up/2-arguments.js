#!/usr/bin/node

// This script prints a message depending of the number of arguments passed
const count = process.argv.length;

if (count === 2) {
  console.log('No argument');
} else if (count === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
