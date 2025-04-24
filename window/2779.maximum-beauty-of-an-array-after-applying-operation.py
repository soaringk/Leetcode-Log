#
# @lc app=leetcode id=2779 lang=python3
#
# [2779] Maximum Beauty of an Array After Applying Operation
#
'''
由于选的是子序列，且操作后子序列的元素都相等，所以元素顺序对答案没有影响，可以先对数组排序。

示例 1 排序后 nums=[1,2,4,6]。由于每个数 x 可以改成闭区间 [x−k,x+k] 中的数，我们把示例 1 的每个数看成闭区间，
也就是题目要求的「由相等元素组成的最长子序列」，相当于选出若干闭区间，这些区间的交集不为空。

排序后，选出的区间是连续的，我们只需考虑最左边的区间 [x−k,x+k] 和最右边的区间 [y−k,y+k]，
如果这两个区间的交集不为空，那么选出的这些区间的交集就不为空。也就是说，要满足

x + k ≥ y - k，即 y - x ≤ 2k

于是原问题等价于：排序后，找最长的连续子数组，其最大值减最小值 ≤2k。
由于数组是有序的，相当于子数组的最后一个数减去子数组的第一个数 ≤2k。
'''

# @lc code=start
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = left = 0
        for right, x in enumerate(nums):
            while x - nums[left] > k * 2:
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# @lc code=end

