#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i, remain):
            if remain == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return

            if remain < candidates[i]:
                return
            # 枚举选哪个
            # 注意这里是递归到 j 不是 j+1，表示 candidates[j] 可以重复选取。
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                dfs(j, remain - candidates[j])
                path.pop()  # 恢复现场

        dfs(0, target)

        return ans

    # 产生重复的原因是：在每一个结点，做减法，展开分支的时候，由于题目中说 每一个元素可以重复使用，我们考虑了 所有的 候选数，因此出现了重复的列表。
    # 一种简单的去重方案是借助哈希表的天然去重的功能，但实际操作一下，就会发现并没有那么容易。
    # 可不可以在搜索的时候就去重呢？
    # 答案是可以的。遇到这一类相同元素不计算顺序的问题，我们在搜索的时候就需要**按某种顺序搜索**。
    # 具体的做法是：每一次搜索的时候设置 下一轮搜索的起点 begin，请看下图。即：从每一层的第 2 个结点开始，都不能再搜索产生同一层结点已经使用过的 candidate 里的元素。
    # 友情提示：如果题目要求，结果集不计算顺序，此时需要按顺序搜索，才能做到不重不漏。「力扣」第 47 题（ 全排列 II ）、「力扣」第 15 题（ 三数之和 ）也使用了类似的思想，使得结果集没有重复。
    def combinationSumDupcalite(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(path):
            s = sum(path)
            if s >= target:
                if s == target:
                    ans.append(path[:])
                return
            for c in candidates:
                path.append(c)
                dfs(path)
                path.pop()

        dfs([])

        return ans


# @lc code=end
Solution().combinationSum([2, 3, 6, 7], 7)
