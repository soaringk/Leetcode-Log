#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
from typing import List


# @lc code=start
class Solution:
    # search in [left, right)
    # greedy partition
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = left + (right - left) // 2
            if self.can_split(nums, m, mid):
                right = mid
            else:
                left = mid + 1

        return right

    def can_split(self, nums: List[int], m: int, mid: int):
        cnt = 1
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum > mid:
                cur_sum = nums[i]
                cnt += 1
                if cnt > m:
                    return False

        return True



    def splitArrayDP(self, nums: List[int], m: int) -> int:
        n = len(nums)
        if n == m:
            return max(nums)

        dp = [[float('inf') for _ in range(m)] for _ in range(n)]
        tmp = 0
        for i in range(n):
            dp[i][0] = sum(nums[:i + 1])
            if tmp < m:
                dp[i][tmp] = max(nums[:i + 1])
                tmp += 1

        for i in range(2, n):
            for j in range(1, m):
                for k in range(j - 1, i):
                    val = max(dp[k][j - 1], sum(nums[k + 1:i + 1]))
                    dp[i][j] = min(val, dp[i][j])

        return dp[n - 1][m - 1]


# @lc code=end
s = Solution()
a = s.splitArray([2, 3, 1, 2, 4, 3], 5)
