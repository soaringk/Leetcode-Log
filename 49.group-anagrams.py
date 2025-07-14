#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import List

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            d[sorted_s].append(s)
        return list(d.values())



# @lc code=end
