#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const count = {};
  const jsonData = JSON.parse(body);
  jsonData.forEach(item => {
    const userId = item.userId;
    if (item.completed) {
      if (count[userId]) {
        count[userId]++;
      } else {
        count[userId] = 1;
      }
    }
  });
  console.log(count);
});
