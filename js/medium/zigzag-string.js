const convert = (s, numRows) => {
  if (s.length == 1 || numRows <= 1) {
    return s;
  }
  let res = "";
  for (let r = 0; r < numRows; r++) {
    increment = 2 * (numRows - 1);
    for (let i = r; i < s.length; i += increment) {
      res += s[i];
      if (r > 0 && r < numRows - 1 && i + increment - 2 * r < s.length) {
        res += s[i + increment - 2 * r];
      }
    }
  }
  return res;
};

console.log(convert("PAYPALISHIRING", 3));
