#!/usr/bin/node
// Script that compute the number of
// tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.error(error);
  if (response && response.statusCode === 200) {
    const toDos = JSON.parse(body);
    const output = {};

    for (const toDo of toDos) {
      if (toDo.completed === true) {
        if (output[toDo.userId] === undefined) {
          output[toDo.userId] = 1;
        } else {
          output[toDo.userId]++;
        }
      }
    }
    console.log(output);
  }
});
