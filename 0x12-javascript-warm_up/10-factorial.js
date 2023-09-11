#!/usr/bin/node

const args = process.argv;

const fac = (x) => {
  if (x <= 1) {
    return 1;
  } else {
    return x * fac(x - 1);
  }
};

console.log(fac(parseInt(args[2])));
