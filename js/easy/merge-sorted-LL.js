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

var sortLists = function (l1, l2) {
  let result = new ListNode(0);
  let temp_head = result;
  while (l1 || l2) {
    l1_val = l1 ? l1.val : 0;
    l2_val = l2 ? l2.val : 0;

    if (l1 || l1?.val < l2?.val) {
      result.next = new ListNode(l1.val);
      l1 = l1.next;
      result = result.next;
    } else if (l2 || l1?.val > l2?.val) {
      result.next = new ListNode(l2.val);
      l2 = l2.next;
      result = result.next;
    }
  }
  return temp_head.next;
};

let printAll = (head) => {
  while (head) {
    console.log(head.val);
    head = head.next;
  }
};
let l7 = new ListNode(6);
let l6 = new ListNode(5, l7);
let l5 = new ListNode(4, l6);
let l4 = new ListNode(3, l5);
let l3 = new ListNode(2, l4);
let li2 = new ListNode(1, l3);
let li1 = new ListNode(0, li2);

let l11 = new ListNode(10);
let l10 = new ListNode(9, l11);
let l9 = new ListNode(8, l10);
let l8 = new ListNode(7, l9);

let result11 = sortLists(li1, l8);
printAll(result11);

let l22 = new ListNode(0);
let l33 = new ListNode(0);
let result2 = sortLists(l22, l33);
printAll(result2);
