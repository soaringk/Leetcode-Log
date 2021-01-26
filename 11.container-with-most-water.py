#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc code=start
class Solution:
    def maxArea(self, height) -> int:
        mArea = 0
        l = 0
        r = len(height) - 1
        while (l < r):
            area = min(height[l], height[r]) * (r - l)
            mArea = max(mArea, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return mArea


# @lc code=end
s = Solution()
s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
