/**

The KMP algorithm first calculates the longest prefix suffix array which enable us to keep a record of 
previously found matches and not check them again therefore reducing complexity

Example: mississippi, issip

issi occurs in the string twice so we need to keep check that the first one is not the same as last

a a a c a a a a
p i
[0,1]

a a a x a a a a
  p i
[0,1,2]

a a a x a a a a
    p i
[0,1,2]

a a a x a a a a
  p   i
[0,1,2]

a a a x a a a a
p     i
[0,1,2,0]

a a a x a a a a
p       i
[0,1,2,0,1]

a a a x a a a a
  p       i       
[0,1,2,0,1,2]

a a a x a a a a
    p       i       
[0,1,2,0,1,2,3]

a a a x a a a a
      p       i       
[0,1,2,0,1,2,3]

a a a x a a a a
    p         i       
[0,1,2,0,1,2,3,3]

Complexity for creating LPS is 2 * N where N = len of needle
*/

const strStr = (haystack, needle) => {
  if (needle === "") return 0;
  let lps = new Array(needle.length).fill(0);
  let j = 1;
  let prevLPS = 0;

  while (j < needle.length) {
    if (needle[prevLPS] == needle[j]) {
      lps[j] = prevLPS + 1;
      prevLPS++;
      j++;
    } else if (prevLPS == 0) {
      j++;
    } else {
      prevLPS = lps[prevLPS - 1];
    }
  }

  let i = 0; // ptr for haystack
  j = 0; // prt for needle

  while (i < haystack.length) {
    if (haystack[i] == needle[j]) {
      i++;
      j++;
    } else if (j == 0) {
      i++;
    } else {
      j = lps[j - 1];
    }
    if (j == needle.length) {
      return i - j;
    }
  }
  return -1;
};

console.log(strStr("aaacaaaa", "aaaa"));
console.log(strStr("mississippi", "issip"));
