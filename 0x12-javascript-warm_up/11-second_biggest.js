#!/usr/bin/node
const arr = [];
const argLength = Number(process.argv.length);
if (argLength === 2 || argLength === 3) {
  console.log(0);
} else {
  for (let i = 2; i < argLength; i++) {
    arr.push(process.argv[i]);
  }
  arr.sort(function (a, b) {
    if (a === Infinity) { return 1; } else if (isNaN(a)) { return -1; } else { return a - b; }
  });
  console.log(arr[arr.length - 2]);
}
