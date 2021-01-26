#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#


# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        sign = 1
        MAX, MIN = 2147483647, -2147483648
        result, pos = 0, 0
        length = len(str)
        while pos < length and str[pos] == ' ':
            pos += 1
        if pos < length and str[pos] == '-':
            sign = -1
            pos += 1
        elif pos < length and str[pos] == '+':
            pos += 1
        while pos < length and ord(str[pos]) >= ord('0') and ord(
                str[pos]) <= ord('9'):
            num = ord(str[pos]) - ord('0')
            if result > MAX // 10 or (result == MAX // 10 and num > 7):
                if sign == -1:
                    return MIN
                return MAX
            result = result * 10 + num
            pos += 1
        return sign * result


# @lc code=end
