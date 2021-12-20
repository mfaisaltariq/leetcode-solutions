// Given an integer x, return true if x is palindrome integer.

// An integer is a palindrome when it reads the same backward as forward.

// For example, 121 is a palindrome while 123 is not.

const isPalindrome = (num) => {
  // All negative nos are not palindrom, all nos ending with 0 are not palindrome
  // All single digit nos including 0 is palindrome
  if (num < 0 || (num % 10 == 0 && num != 0)) return false;
  if (num == 0 || num < 10) return true;
  let numStr = String(num);
  let strLen = numStr.length;
  for (let i = 0; i < strLen / 2; i++) {
    if (numStr[i] !== numStr[strLen - (i + 1)]) {
      return false;
    }
    return true;
  }
};

const isPalindromeWithoutConvertingToString = (num) => {
  // All negative nos are not palindrom, all nos ending with 0 are not palindrome
  // All single digit nos including 0 is palindrome
  if (num < 0 || (num % 10 == 0 && num != 0)) return false;
  if (num == 0 || num < 10) return true;
  // We split the number in half and then we
  let revertedNumber = 0;
  while (num > revertedNumber) {
    revertedNumber = Math.trunc(revertedNumber * 10 + (num % 10));
    num = Math.trunc(num / 10);
    console.log(revertedNumber, num, "here");
  }
  // When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
  // For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
  // since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
  console.log(revertedNumber);
  console.log(num);
  return num == revertedNumber || num == Math.trunc(revertedNumber / 10);
};

console.log(isPalindromeWithoutConvertingToString(98989));
// console.log(isPalindromeWithoutConvertingToString(123));
