#!/usr/bin/env node

exports.esrever = function (list) {
  const revsList = [];
  let i = 0;

  for (i = list.lenght - 1; i >= 0; i--) {
    revsList.push(list[i]);
  }
  return revsList;
};
