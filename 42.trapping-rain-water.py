#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        left = 0
        right = len(height) - 1
        res = 0

        l_max = height[left]
        r_max = height[right]

        while left <= right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])

            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1

        return res


# @lc code=end
