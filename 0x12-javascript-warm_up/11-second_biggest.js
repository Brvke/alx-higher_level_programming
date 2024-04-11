#!/usr/bin/node

const argl = process.argv.length;
if (argl <= 3) console.log(0);
else {
  const Narr = process.argv
    .splice(2, argl - 2)
    .map((el) => parseInt(el))
    .filter((el, idx, arr) => el !== Math.max(...arr));

  console.log(Math.max(...Narr));
}
