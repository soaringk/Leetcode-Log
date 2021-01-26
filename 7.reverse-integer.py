#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2147483647
        isPos = 1
        if x < 0:
            x *= -1
            isPos = -1
        rev = 0
        while x > 0:
            rem = x % 10
            if rev > MAX / 10 or (rev == MAX / 10 and rem > 7):
                return 0
            x //= 10
            rev = rev * 10 + rem
        return rev * isPos


# @lc code=end
