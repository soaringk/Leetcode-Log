#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes: return 0
        sort = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        height = []
        for i in range(len(sort)):
            height.append(sort[i][1])
        return self.lengthOfLIS(height)

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(len(dp)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
# @lc code=end
