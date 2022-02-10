const reverse = (num) => {
  if (num > -10 && num < 10) {
    return num;
  }
  let isNegative = false;
  if (num < 0) {
    isNegative = true;
    num *= -1;
  }
  let reversedNum = 0;
  while (num >= 10) {
    reversedNum = reversedNum * 10 + (num % 10);
    num = Math.trunc(num / 10);
  }

  reversedNum = reversedNum * 10 + num;
  if (isNegative) {
    reversedNum *= -1;
  }
  let range = 2 ** 31;
  if (reversedNum > range - 1 && reversedNum < -range) {
    return 0;
  }
  return reversedNum;
};

console.log(reverse(-123456));
