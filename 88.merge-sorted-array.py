#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        p1 = m - 1  # [1, 2, (3), 0, (0)], m = 3
        p2 = n - 1  # [1, (2)], n = 2

        while p >= 0 and p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p1 >= 0:
            nums1[p] = nums1[p1]
            p1 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# @lc code=end
s = Solution()
s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
