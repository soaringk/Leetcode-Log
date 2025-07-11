#
# @lc app=leetcode id=2730 lang=python3
#
# [2730] Find the Longest Semi-Repetitive Substring
#

# @lc code=start
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans, left, same = 1, 0, 0
        for right in range(1, len(s)):
            same += s[right] == s[right - 1]
            if same > 1:  # same == 2
                left += 1
                while s[left] != s[left - 1]:
                    left += 1
                same = 1
            ans = max(ans, right - left + 1)
        return ans
   
# @lc code=end

