#!/usr/bin/node

const request = require('request');

request.get('https://swapi-api.alx-tools.com/api/people/18/',
  (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      try {
        const filmData = JSON.parse(body);
        const numFilms = filmData.films;
        console.log(numFilms.length);
      } catch (parseError) {
        console.error('An error occurred while parsing the JSON response:',
          parseError);
      }
    }
  });
