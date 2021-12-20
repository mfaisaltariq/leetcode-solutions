/** 
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers2 = function (l1, l2) {
  let result = new ListNode(0);
  let temp_head = result;
  let carry = 0;
  let sum = 0;
  let l1_val = 0;
  let l2_val = 0;
  while (l1 || l2 || carry) {
    l1_val = l1 ? l1.val : 0;
    l2_val = l2 ? l2.val : 0;

    sum = l1_val + l2_val + carry;
    if (sum >= 10) {
      sum = sum % 10;
      carry = 1;
    } else {
      carry = 0;
    }
    result.next = new ListNode(sum);
    result = result.next;
    l1 = l1 ? l1.next : null;
    l2 = l2 ? l2.next : null;
  }
  return temp_head.next;
};

let printAll = (head) => {
  while (head) {
    console.log(head.val);
    head = head.next;
  }
};
let l7 = new ListNode(9);
let l6 = new ListNode(9, l7);
let l5 = new ListNode(9, l6);
let l4 = new ListNode(9, l5);
let l3 = new ListNode(9, l4);
let l2 = new ListNode(9, l3);
let l1 = new ListNode(9, l2);

let l11 = new ListNode(9);
let l10 = new ListNode(9, l11);
let l9 = new ListNode(9, l10);
let l8 = new ListNode(9, l9);

let result = addTwoNumbers2(l1, l8);
printAll(result);

let l22 = new ListNode(0);
let l33 = new ListNode(0);
let result2 = addTwoNumbers2(l22, l33);
console.log("result2", result2);

// 2,4,9
// 5,6,4
// 7,0,4,1

// #Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// # 9999999
// # 9999
// # 89990001
