#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from typing import List

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 输入的视角
        n = len(s)
        ans = []
        path = []

        # start 表示当前这段回文子串的开始位置
        def dfs(i: int, start: int) -> None:
            if i == n: # 子问题：已经枚举完了分隔符出现的问题，最后一定是在字符串末尾。如果最后一段不是回文串，那么递归栈会回溯到上一层，不会加入答案集合
                ans.append(path.copy())  # 复制 path
                return

            # 当前操作：不选 i 和 i+1 之间的逗号（i=n-1 时一定要选）
            if i < n - 1:
                dfs(i + 1, start)

            # 当前操作：选 i 和 i+1 之间的逗号 s[start...i] 是否为回文串，如果已经不是，不需要加入答案集合
            t = s[start: i + 1]
            if t == t[::-1]:  # 判断是否回文
                path.append(t)
                dfs(i + 1, i + 1)  # 下一个子问题：枚举子串 s[i+1...k]
                path.pop()  # 恢复现场

        dfs(0, 0)
        return ans

# @lc code=end

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 答案的视角（相当于枚举子串结束位置）
        n = len(s)
        ans = []
        path = []

        def dfs(i: int) -> None:
            if i == n: # 子问题，已经枚举完了所有字符，复制 path
                ans.append(path.copy())
                return
            for j in range(i, n):  # 当前操作：枚举子串的结束位置 s[i...j] 作为回文子串
                t = s[i: j + 1]
                if t == t[::-1]:  # 判断是否回文，如果已经不是，不需要加入答案集合
                    path.append(t)
                    dfs(j + 1) # 下一个子问题：枚举下一个子串 s[j+1...k]
                    path.pop()

        dfs(0)
        return ans
