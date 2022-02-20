const maxArea = (height) => {
  let left = 0;
  let right = height.length - 1;
  let area = 0;
  while (left < right) {
    temp = Math.min(height[left], height[right]) * (right - left);
    area = Math.max(area, temp);

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }
  return area;
};

console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]));
