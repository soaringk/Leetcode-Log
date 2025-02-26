#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List


# @lc code=start
class Solution:
    choices = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    def letterCombinations(self, digits: str) -> List[str]:
        # 解决单纯的嵌套循环，循环层级有限的问题
        # 回溯通过递归，增量构造答案集合
        # 1.当前操作：枚举 path[i] 的选择
        # 2.子问题：构造 >= i 部分的答案
        # 3.下一个子问题：狗仔 >= i+1 部分的答案
        # dfs(i) -> dfs(i+1), i 的含义为还需要枚举 i 及其之后的选择
        n = len(digits)
        if n == 0:
            return []

        ans = []
        path = [''] * n
        def dfs(i):
            if i == n: # 递归终止条件（也是子问题？因为当 i != n 时的子问题不需要进行处理）
                ans.append(''.join(path))
                return
            for c in self.choices[int(digits[i])]: # 当前操作
                path[i] = c
                dfs(i + 1) # 下一个子问题

        dfs(0)
        return ans
# @lc code=end
ret = Solution().letterCombinations('23')
print(ret)
