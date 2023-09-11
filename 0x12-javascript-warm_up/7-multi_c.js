#!/usr/bin/node

const args = process.argv.slice(2);
const x = args[0];
let i = 0;
if (x == null || isNaN(x)) {
  console.log('Missing number of occurrences');
}
while (i < x) {
  console.log('C is fun');
  i += 1;
}
