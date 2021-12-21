/** 
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

SOLUTION:
We have to find the highest common prefix in a given array of string so that means we just need to check
the least common elements of the array. We can sort the array and then check only first and last element
to find the largest common prefix.

complexity is log o(n) * min(range)
*/

let longestCommonPrefix = (strs) => {
  sortedList = strs.sort();
  let smallestElement = Math.min(
    sortedList[0].length,
    sortedList[sortedList.length - 1].length
  );
  longestPrefix = "";
  for (let i = 0; i < smallestElement; i++) {
    if (sortedList[0][i] === sortedList[sortedList.length - 1][i]) {
      longestPrefix += sortedList[0][i];
    } else {
      return longestPrefix;
    }
  }
  return longestPrefix;
};

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
console.log(longestCommonPrefix(["dog", "racecar", "car"]));
