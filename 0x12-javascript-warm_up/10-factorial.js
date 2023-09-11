#!/usr/bin/node

const args = process.argv;

function fac (x) {
  if (isNaN(parseInt(x))) {
    return 1;
  }
  if (x <= 1) {
    return 1;
  } else {
    return x * fac(x - 1);
  }
}

console.log(fac(parseInt(args[2])));
