/**
 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
*/

// test case [3,3] with target 6 is an edge case keep it in the mind

const twoSum = (nums, target) => {
  let my_map = {};
  let result = [];
  [...nums].forEach((num, index) => {
    if (my_map[num]) {
      result.push(nums.indexOf(target - num));
      result.push(index);
      return result;
    } else {
      let a = target - num;
      my_map[a] = num;
    }
  });

  return result;
};

console.log(twoSum([3, 3], 6));
