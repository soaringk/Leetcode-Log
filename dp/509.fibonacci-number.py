#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n < 1: return 0
        if n == 1 or n == 2: return 1
        prev = 1
        curr = 1
        for i in range(3, n + 1):
            nex = prev + curr
            prev = curr
            curr = nex
        return curr

# @lc code=end
