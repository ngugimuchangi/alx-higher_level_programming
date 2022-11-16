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
      }
      if (toDo.userId !== userId || toDos.indexOf(toDo) === toDos.length - 1) {
        output[userId] = count;
        count = 1;
        userId = toDo.userId;
      }
    }

//    const keys = Object.keys(output);

//    for (const userId of keys) {
//      if (keys.indexOf(userId) === 0) {
//        console.log(`{ '${userId}': ${output[userId]}`);
//      } else if (keys.indexOf(userId) === keys.length - 1) {
//        console.log(`  '${userId}': ${output[userId]} }`);
//      } else {
//        console.log(`  '${userId}': ${output[userId]}`);
//      }
//    }
    console.log(output);
  }
});
