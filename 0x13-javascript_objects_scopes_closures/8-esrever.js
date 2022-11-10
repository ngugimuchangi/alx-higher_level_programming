#!/usr/bin/node
// function that returns a reversed version of a list

exports.esrever = function (list) {
  let fIdx = 0;
  let lIdx = list.length - 1;

  while (fIdx < lIdx) {
    [list[fIdx], list[lIdx]] = [list[lIdx], list[fIdx]];
    fIdx++;
    lIdx--;
  }
  return list;
};
