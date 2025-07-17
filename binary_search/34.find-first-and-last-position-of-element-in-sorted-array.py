#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
from typing import List

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left_bound():
            if len(nums) == 0:
                return -1
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1

            if l >= len(nums) or nums[l] != target:
                return -1
            return l

        def find_right_bound():
            if len(nums) == 0:
                return -1
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1

            if r >= len(nums) or nums[r] != target:
                return -1
            return r

        left_bound = find_left_bound()
        right_bound = find_right_bound()

        return [left_bound, right_bound]


    # 要想找到 ≤ target 的最后一个数，可以先找到这个数的右边相邻数字，也就是 > target 的第一个数。
    # 在整数前提下，> target 等价于 ≥ target + 1
    
    # lower_bound 返回最小的满足 nums[i] >= target 的下标 i
    # 如果数组为空，或者所有数都 < target，则返回 len(nums)
    # 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 闭区间 [left, right]
        while left <= right:  # 区间不为空
            # 循环不变量：
            # nums[left-1] < target
            # nums[right+1] >= target
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1  # 范围缩小到 [left, mid-1]
            else:
                left = mid + 1  # 范围缩小到 [mid+1, right]
        # 循环结束后 left = right+1
        # 此时 nums[left-1] < target 而 nums[left] = nums[right+1] >= target
        # 所以 left 就是第一个 >= target 的元素下标
        return left
    
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        start = self.lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]  # nums 中没有 target
        # 如果 start 存在，那么 end 必定存在
        end = self.lower_bound(nums, target + 1) - 1
        return [start, end]

# @lc code=end
S = Solution()
S.searchRange([5, 7, 7, 8, 8, 10], 8)
