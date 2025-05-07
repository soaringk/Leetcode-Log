#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
from typing import List

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []
        # 其实是不必要的，因为题干要求返回唯一集合，所以如果某元素与左边元素相等，说明该搜索分支重复，直接跳过，完全不需要判断有没有用过
        # used = [False for _ in range(len(candidates))]
        def backtrack(start, target):
            if target == 0:
                ans.append(path[:])
                return
            if target < 0 or len(path) == len(candidates):
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]: # and not used[i-1]:
                    continue
                path.append(candidates[i])
                # used[i] = True
                backtrack(i+1, target-candidates[i])
                path.pop()
                # used[i] = False
        backtrack(0, target)
        return ans
# @lc code=end
Solution().combinationSum2([10,1,2,7,6,1,5],8)