#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
from typing import List
# @lc code=start
import random
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # partition
        size = len(nums)

        target = size - k
        left = 0
        right = size - 1
        while True:
            index = self.__partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                # 下一轮在 [index + 1, right] 里找
                left = index + 1
            else:
                right = index - 1

    #  循环不变量：[left + 1, j] < pivot
    #  (j, i) >= pivot
    def __partition(self, nums, left, right):
        # randint 是包括左右区间的
        random_index = random.randint(left, right)
        nums[random_index], nums[left] = nums[left], nums[random_index]

        pivot = nums[left]

        lt = left + 1
        rt = right

        while True:
            while lt <= rt and nums[lt] < pivot:
                lt += 1
            while lt <= rt and nums[rt] > pivot:
                rt -= 1

            if lt > rt:
                break
            nums[lt], nums[rt] = nums[rt], nums[lt]
            lt += 1
            rt -= 1

        nums[left], nums[rt] = nums[rt], nums[left]
        return rt

    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        # heap
        neg_nums = [-x for x in nums]
        heapq.heapify(neg_nums)
        while k > 1:
            heapq.heappop(neg_nums)
            k -= 1
        return -heapq.heappop(neg_nums)

# @lc code=end
s = Solution()
s.findKthLargest([3,2,1,5,6,4], 2)
