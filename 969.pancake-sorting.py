#
# @lc app=leetcode id=969 lang=python3
#
# [969] Pancake Sorting
#
from typing import List
# @lc code=start
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if sorted(arr) == arr:
            return []

        res = []

        def reversePancake(arr, n):
            if n == 1:
                return
            max_val = max(arr[:n])
            max_idx = arr.index(max_val)
            if not max_idx == n - 1:
                if max_idx != 0:
                    res.append(max_idx + 1)
                    arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
                res.append(n)
                arr[:n] = arr[:n][::-1]

            reversePancake(arr, n - 1)

        reversePancake(arr, len(arr))
        return res




# @lc code=end
s = Solution()
s.pancakeSort([2, 1, 3])
