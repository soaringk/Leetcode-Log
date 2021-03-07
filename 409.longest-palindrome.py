#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = dict()
        for i in s:
            counts[i] = counts.get(i, 0) + 1

        res = 0
        for k in counts:
            res += counts[k] // 2 * 2
            if counts[k] % 2 == 1 and res % 2 == 0:
                res += 1
        return res

# @lc code=end
s = Solution()
s.longestPalindrome("abccccdd")
