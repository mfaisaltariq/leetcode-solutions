/**
 Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
 */

const getIndex = (arr, num) => {
  start = 0;
  end = arr.length - 1;
  mid = start + end / 2;
  while (start <= end) {
    let mid = Math.floor((start + end) / 2);

    if (arr[mid] == num) return mid;
    else if (arr[mid] < num) start = mid + 1;
    else end = mid - 1;
  }
  return end + 1;
};
