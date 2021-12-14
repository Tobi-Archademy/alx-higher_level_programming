#!/usr/bin/node
const myArgs = require('process').argv;
const argPassed = myArgs.slice(2, 3).toString();

if (argPassed) {
  console.log(argPassed);
} else {
  console.log('No argument');
}
