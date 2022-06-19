from typing import List 
from collections import defaultdict
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = defaultdict(list)
    
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


