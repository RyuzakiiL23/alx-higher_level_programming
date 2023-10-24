#!/usr/bin/node

const request = require('request');
const filmsUrl = process.argv[2];
const newUrl = filmsUrl.replace('/films', '/people/18');

request.get(newUrl,
  (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      try {
        const filmData = JSON.parse(body);
        const numFilms = filmData.films;
        console.log(numFilms.length.toString());
      } catch (parseError) {
        console.error('An error occurred while parsing the JSON response:',
          parseError);
      }
    }
  });
