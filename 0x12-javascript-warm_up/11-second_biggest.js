#!/usr/bin/node

const args = process.argv;
const values = process.argv.slice(2);
if (args.length < 4) {
  console.log('0');
} else {
  for (const x in values) {
    values[x] = parseInt(values[x]);
  }
  values.sort(function (a, b) {
    return a - b;
  });
  values.reverse();
  console.log(values[1]);
}
