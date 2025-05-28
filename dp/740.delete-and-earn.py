#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#


# @lc code=start
class Solution:
    # 将 nums 转化成值域数组后变成打家劫舍
    # 直接 dp 也可以，但是需要排序，所以复杂度必定为 O(nlogn)
    # f[i] = f[i-1] + nums[i] * 出现次数 if f[i+1] > f[i] + 1，直接追加
    # f[i] = max(f[i-1], f[i-2] + nums[i] * 出现次数) if f[i+1] == f[i] + 1，需要做选择，因此有转移
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 转换成值域数组 s[i] 为 nums 中值为 i 的数字总和
        s = [0] * (max(nums) + 1)
        for i in nums:
            s[i] += i  # 统计等于 x 的元素之和

        n = len(s)
        dp = [0] * (n + 2)
        dp[1] = s[0]
        for i in range(n):
            dp[i+2] = max(dp[i + 1], dp[i] + s[i])
        return dp[n+1]


# @lc code=end
