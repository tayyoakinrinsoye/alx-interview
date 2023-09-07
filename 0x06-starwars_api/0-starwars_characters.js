#!/usr/bin/node

const request = require('request');

const id = process.argv[2] + '/';
const baseUrl = "https://swapi-api.alx-tools.com/films/";

request(baseUrl + id, async function (err, res, body) {
  if (err) return console.error(err);

  const listUrl = JSON.parse(body).characters;

  for (const list of listUrl) {
    await new Promise(()=>{
      request(list, function(err, res, body){
        if (err) return console.error(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});