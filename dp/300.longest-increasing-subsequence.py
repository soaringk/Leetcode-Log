#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 定义 f[i] 以 nums[i] 结尾的 LIS
        # f[i] = max(f[j]) + 1, for j in range(i)
        dp = [1 for _ in range(len(nums))]
        for i in range(len(dp)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def patienceGame(self, nums):
        top = [1 for _ in range(len(nums))]
        piles = 0
        for i in range(len(nums)):
            poker = nums[i]

            ### 搜索左侧边界的二分查找
            left = 0
            right = piles
            while left < right:
                mid = (left + right) // 2
                if top[mid] > poker:
                    right = mid
                elif top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid

            if left == piles:
                piles += 1
            # 把该牌放至顶部
            top[left] = poker

        return piles

# @lc code=end
