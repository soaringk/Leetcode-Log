#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
from typing import List

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]: # [0, mid] 无旋转
                if nums[0] <= target < nums[mid]: # 位于前面有序的这一段
                    r = mid - 1
                else:                # 向后
                    l = mid + 1
            else:                    # [0, mid] 有旋转
                if nums[mid] < target <= nums[len(nums) - 1]:   # 位于后面有序的这一段
                    l = mid + 1
                # elif target <= nums[mid] < nums[0]:  # target 在旋转位置到 mid 之间
                #     r = mid - 1
                # elif nums[mid] < nums[0] <= target:  # target 在 0 到旋转位置之间
                #     r = mid - 1
                else:
                    r = mid - 1

        return -1

    def search_simplify(self, nums, target):
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        check_1 = nums[0] <= target
        while l < r:
            mid = l + (r - l) // 2
            check_2 = target <= nums[mid]
            check_3 = nums[mid] < nums[0]
            if check_1 ^ check_2 ^ check_3:
                l = mid + 1
            else:
                r = mid

        return l if (l == r and nums[l] == target) else -1



# @lc code=end
s = Solution()
s.search([4,5,6,7,0,1,2], 0)
