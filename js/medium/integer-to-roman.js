const intRoman = (num) => {
  let dict = [
    ["I", 1],
    ["IV", 4],
    ["V", 5],
    ["IX", 9],
    ["X", 10],
    ["XL", 40],
    ["L", 50],
    ["XC", 90],
    ["C", 100],
    ["CD", 400],
    ["D", 500],
    ["CM", 900],
    ["M", 1000],
  ];
  let res = "";
  for (let i = dict.length - 1; i >= 0; i--) {
    if (Math.floor(num / dict[i][1])) {
      console.log(num / dict[i][1]);
      repeat = Math.floor(num / dict[i][1]);
      res += dict[i][0].repeat(repeat);
      num = num % dict[i][1];
      console.log(num);
    }
  }
  return res;
};

console.log(intRoman(58));
