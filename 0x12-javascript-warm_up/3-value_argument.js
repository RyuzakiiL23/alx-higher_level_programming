#!/usr/bin/node

const args = process.argv.slice(2);
const message = args[0];

if (message == null) {
  console.log('No argument');
} else {
  console.log(message);
}
