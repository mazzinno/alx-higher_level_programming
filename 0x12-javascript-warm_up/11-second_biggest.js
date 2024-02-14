#!/usr/bin/node
function nextBiggest (arr) {
  let maxNum = 0; let result = 0;

  for (const value of arr) {
    const nr = Number(value);

    if (nr > maxNum) {
      [result, maxNum] = [maxNum, nr];
    } else if (nr < maxNum && nr > result) {
      result = nr;
    }
  }

  return result;
}

console.log(nextBiggest(process.argv));
