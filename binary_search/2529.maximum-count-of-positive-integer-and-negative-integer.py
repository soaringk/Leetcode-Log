#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#


# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < 0:
                l = mid + 1
            else:
                r = mid - 1
        while r + 1 < len(nums) and nums[r + 1] == 0:
            r += 1
        neg = l
        pos = len(nums) - (r + 1)
        return max(neg, pos)


# @lc code=end
s = Solution()
print(s.maximumCount([-3, -2, -1, 0, 0, 1, 2]))
