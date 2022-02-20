const myAtoi = (s) => {
  let isNegative = false;
  if (s[0] == "-") {
    isNegative = true;
    s = s.slice(1, s.length);
  } else if (s[0] == "-") {
    s = s.slice(1, s.length);
  }
  let num = 0;
  for (let char of s) {
    if (char >= "0" && char <= "9") {
      //   console.log("here", num, char);
      num = num * 10 + parseInt(char);
    } else {
      break;
    }
  }
  if (isNegative) num *= -1;
  return num;
};

console.log(myAtoi("-100de"));
console.log(myAtoi("9203"));
console.log(myAtoi("-67400 de"));
