#!/usr/bin/node
// Script ath compute the number of
// tasks completed by user id

const request = require('request');
const url = process.argv[2] + '?completed=true';

request(url, (error, response, body) => {
  if (error) throw error;
  if (response) {
    const toDos = JSON.parse(body);
    const output = {};
    let count = 0;
    let userId = toDos[0].userId;
    for (const toDo of toDos) {
      if (toDo.userId === userId) {
        count++;
      } else {
        output[userId] = count;
        count = 1;
        userId = toDo.userId;
      }
    }
    console.log(JSON.stringify(output));
  }
});
