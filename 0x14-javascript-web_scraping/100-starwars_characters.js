#!/usr/bin/node

const request = require('request');
const idFilm = process.argv[2];
const urlFilm = `https://swapi-api.alx-tools.com/api/films/${idFilm}`;
request.get(urlFilm, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const jsonData = JSON.parse(body);
    jsonData.characters.forEach(item => {
      request.get(item, (error, response, body) => {
        if (!error) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
