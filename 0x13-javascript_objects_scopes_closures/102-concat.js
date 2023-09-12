#!/usr/bin/node
const fs = require('fs');

const fileAContents = fs.readFileSync(process.argv[2]).toString();
const fileBContents = fs.readFileSync(process.argv[3]).toString();
const concatenatedContents = fileAContents + fileBContents;
fs.writeFileSync(process.argv[4], concatenatedContents);
