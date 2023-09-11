#!/usr/bin/node

const args = process.argv;
const x = parseInt(args[2]);

if (isNaN(parseInt(args[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    for (let i = 0; i < x; i++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
