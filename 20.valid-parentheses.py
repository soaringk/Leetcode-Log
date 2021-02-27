#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if not s[0] in ('(', '{', '[') or len(s) % 2 == 1:
            return False

        stack = []
        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
            else:
                try:
                    top = stack.pop()
                except IndexError:
                    return False
                if char == ')' and top == '(':
                    continue
                elif char == '}' and top == '{':
                    continue
                elif char == ']' and top == '[':
                    continue
                else:
                    return False
        return len(stack) == 0


# @lc code=end
s = Solution()
s.isValid('()[]{}')
