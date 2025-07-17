#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 思考：若 ai == ai_1，则删除

        k = 1 # a0 肯定要
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]: # 不是重复项，则保留
                nums[k] = nums[i]
                k += 1

        return k
        
# @lc code=end

