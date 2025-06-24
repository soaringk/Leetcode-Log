#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
from typing import List


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 每次转移只找一个小段，这个小段的最大长度就是最长的那个切分词。因此如果小段的长度超过那个词，小段就不可能在 wordDict 里找到了
        maxLen = max([len(x) for x in wordDict])
        words = set(wordDict)  # 方便快速查找

        # 定义 f[i] 为前 i 个元素是否能被词典拼出来
        # 转移：f[i+1] = f[j] && s[j...i] in wordDict for j in [i-maxLen, i)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # 没有元素时默认可以拼接成

        for i in range(1, n + 1):
            for j in range(i - 1, max(i - maxLen - 1, -1), -1):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]


# @lc code=end
