#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        length = 0
        tmp = x
        while tmp != 0:
            length += 1
            tmp = tmp // 10
        tmp = x
        for i in range(length // 2):
            right = tmp % 10
            left = tmp // (10**(length - 2 * i - 1))
            left = left % 10
            # print left, right
            if left != right:
                return False
            tmp = tmp // 10
        return True


# @lc code=end
