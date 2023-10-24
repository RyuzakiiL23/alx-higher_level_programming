#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];

request.get(url, (error, response, body) => {
fs.writeFile(file, body, { encoding: 'utf8', flag: 'w' }, (err) => {
  if (err) {
    console.error(err);
  }
})
});
