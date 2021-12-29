const lengthOfLongestSubstring = (s) => {
  left_p = 0;
  right_p = 0;
  max = 0;
  let hash_set = new Set();
  while (right_p < s.length) {
    if (!hash_set.has(s[right_p])) {
      hash_set.add(s[right_p]);
      max = Math.max(max, hash_set.size);
      right_p++;
    } else {
      hash_set.delete(s[left_p]);
      left_p++;
    }
  }
  return max;
};

console.log(lengthOfLongestSubstring("abcabcbb"));
