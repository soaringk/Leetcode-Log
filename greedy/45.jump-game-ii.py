#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0

        farthest = 0
        choice = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if choice == i:
                choice = farthest
                cnt += 1

        return cnt


# @lc code=end
