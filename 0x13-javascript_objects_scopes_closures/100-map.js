#!/usr/bin/node

const list = require('./100-main').list;

const newList = list.map((x, index) => x * index);
console.log(list);
console.log(newList);
