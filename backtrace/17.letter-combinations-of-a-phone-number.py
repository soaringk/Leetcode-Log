#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        path = []
        choice = []

        def backtrack(i):
            if i == len(digits):
                choice.append(''.join(path))
            else:
                digit = digits[i]
                for letter in phoneMap[digit]:
                    path.append(letter)
                    backtrack(i + 1)
                    path.pop()

        backtrack(0)

        return choice


# @lc code=end
