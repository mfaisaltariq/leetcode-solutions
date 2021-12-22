/**
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
 */

let isValid = (s) => {
  let stack = [];

  for (char of s) {
    if (char === "(" || char === "{" || char === "[") {
      stack.push(char);
      continue;
    } else {
      if (stack.length === 0) {
        return false;
      }
    }

    let popItem = stack.pop();
    if (popItem === "(" && char !== ")") return false;
    if (popItem === "{" && char !== "}") return false;
    if (popItem === "[" && char !== "]") return false;
  }

  if (stack.length > 0) {
    return false;
  } else return true;
};

console.log(isValid("()[]{}"));
