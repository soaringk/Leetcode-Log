#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        ans = 0
        i = 0
        keys = sorted(symbol_map, key=lambda x: symbol_map[x])
        while i < len(s) - 1:
            next_symbol = s[i + 1]
            current_symbol = s[i]
            if keys.index(next_symbol) > keys.index(current_symbol):
                ans += symbol_map[s[i] + s[i + 1]]
                i += 2
            else:
                ans += symbol_map[s[i]]
                i += 1
        if i == len(s) - 1:
            ans += symbol_map[s[-1]]

        return ans


# @lc code=end
s = Solution()
s.romanToInt('IV')
