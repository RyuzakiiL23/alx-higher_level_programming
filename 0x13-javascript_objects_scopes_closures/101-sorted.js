#!/usr/bin/node

const dict = require('./101-data').dict;
const ids = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (!ids[occurrences]) {
    ids[occurrences] = [];
  }
  ids[occurrences].push(userId);
}
console.log(ids);
