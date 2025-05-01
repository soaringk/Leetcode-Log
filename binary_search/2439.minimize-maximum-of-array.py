#
# @lc app=leetcode id=2439 lang=python3
#
# [2439] Minimize Maximum of Array
#

# @lc code=start
class Solution:
    # 「最小化最大值」就是二分答案的代名词。我们猜测一个上界 limit，即要求操作后所有元素均不超过 limit。
    # 由于 limit 越大越能够满足，越小越无法满足，有单调性，可以二分答案。
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(limit: int) -> bool:
            extra = 0
            for i in range(len(nums) - 1, 0, -1):
                extra = max(nums[i] + extra - limit, 0)
            return nums[0] + extra <= limit
        return bisect_left(range(max(nums)), True, lo=min(nums), key=check)
# @lc code=end
