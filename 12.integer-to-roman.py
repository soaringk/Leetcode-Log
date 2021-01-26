#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_map = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        ans = ''
        keys = sorted(symbol_map, reverse=True)
        for n in keys:
            while num >= n:
                num -= n
                ans += symbol_map[n]

        return ans


# @lc code=end
