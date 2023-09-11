#!/usr/bin/node

const args = process.argv.splice(2);

if (isNaN(parseInt(args[0]))) {
  console.log('Not a number');
} else {
  console.log(parseInt(args[0]));
}
