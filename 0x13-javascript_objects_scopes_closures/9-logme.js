#!/usr/bin/node
/* Function that prints the number of arguents already printed
 * and the new argument value
 */

let call = 0;

exports.logMe = function (item) {
  console.log(`${call++}: ${item}`);
};
