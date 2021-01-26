#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    # Reduce the look up time from O(n) to O(1) by trading space for speed.
    # Time complexity : O(n)
    # Space complexity : O(n)
    def twoSumOnePass(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []

    def twoSum(self, nums, target):
        for i, n in enumerate(nums):
            if target - n in nums and nums.index(target - n) != i:
                return sorted([i, nums.index(target - n)])


s = Solution()
result = s.twoSum([6, 6], 12)
print(result)
Solution()

# @lc code=end
