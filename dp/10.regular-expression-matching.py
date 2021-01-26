#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#


# @lc code=start
class Solution:
    """状态转移方程

    T[i][j]:
    1. T[i-1][j-1] if text[i] == pattern[j] or pattern[j] == '.'
    2. if pattern[j] == '*':
        a. T[i][j-2] -> 0 occurence
        b. T[i-1][j] if text[i] == pattern[j-1] or pattern[j-1] == '.'
    """

    # O(T + P)
    def isMatch(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {
                        text[i], '.'
                    }
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


# @lc code=end
S = Solution()
print(S.TisMatch("aa", "a"))
