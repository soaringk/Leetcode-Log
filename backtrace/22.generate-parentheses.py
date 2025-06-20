#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(S, left, right):
            # 字符串长度一定是 2n，作为终止条件
            if len(S) == 2 * n:
                res.append(''.join(S))
                return
            # 选择 = [加左括号, 加右括号]，但是都有拘束条件

            # 1. 左括号数量不能超过 n
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            # 2. 对于括号字符串的任意前缀，右括号的个数不能超过左括号的个数。
            # 只要左括号比右括号多，继续追加的右括号就是合法的（也可以理解成回溯过程中会不断确保当前序列是有效的，或者最终"可以成为有效"的）
            # 不存在多种类型的括号，所以也不需要检测 `[(])` 这种情况。`(())` 不论怎么互换位置都是有效的
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return res



# @lc code=end
