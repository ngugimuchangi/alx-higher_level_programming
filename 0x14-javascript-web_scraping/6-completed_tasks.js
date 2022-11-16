#!/usr/bin/node
// Script ath compute the number of
// tasks completed by user id

const request = require('request');
const url = process.argv[2] + '?completed=true';

request(url, (error, response, body) => {
  if (error) console.error(error);
  if (response && response.statusCode === 200) {
    const toDos = JSON.parse(body);
    const output = {};

    for (const toDo of toDos) {
      if (output[toDo.userId] === undefined) {
        output[toDo.userId] = 1;
      } else {
        output[toDo.userId]++;
      }
    }
    if (output) console.log(output);
  }
});
