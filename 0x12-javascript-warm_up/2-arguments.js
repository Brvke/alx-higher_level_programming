#!/usr/bin/node

const { argv } = require('process');

const numarg = argv.length;
if (numarg < 3) {
  console.log('No argument');
} else if (numarg === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
