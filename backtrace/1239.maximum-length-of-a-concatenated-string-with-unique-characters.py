#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#
from typing import List


# @lc code=start
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # remove duplicate substring
        for i in range(len(arr) - 1, -1, -1):
            substr = arr[i]
            s = set()
            for ch in substr:
                if ch in s:  # 本身就有重复
                    arr.remove(substr)
                    break
                s.add(ch)

        n = len(arr)
        ans = 0

        def dfs(i, charset):
            # 子问题：是否遍历到候选集的末尾
            if i == n:
                nonlocal ans
                ans = max(ans, len(charset))  # path 内已经保证全是 unique
                return
            # 当前操作：选 or 不选 arr[i] 元素
            # 选的前提是加入子串后不会导致已有选择重复
            chs = set(list(arr[i]))
            if charset.intersection(chs) == set():
                dfs(i + 1, charset.union(chs))
            dfs(i + 1, charset)

        dfs(0, set())
        return ans


# @lc code=end
ret = Solution().maxLength(["aa", "bb"])
