#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(path, left, right):
            # 字符串长度一定是 2n，作为终止条件
            if len(path) == 2 * n:
                res.append(''.join(path))
                return
            # 选择 = [加左括号, 加右括号]，但是都有拘束条件

            # 1. 左括号数量不能超过 n
            if left < n:
                path.append('(')
                backtrack(path, left + 1, right)
                path.pop()
            # 2. 对于括号字符串的任意前缀，右括号的个数不能超过左括号的个数。
            # 只要左括号比右括号多，继续追加的右括号就是合法的（也可以理解成回溯过程中会不断确保当前序列是有效的，或者最终"可以成为有效"的）
            # 不存在多种类型的括号，所以也不需要检测 `[(])` 这种情况。`(())` 不论怎么互换位置都是有效的
            if right < left:
                path.append(')')
                backtrack(path, left, right + 1)
                path.pop()

        backtrack([], 0, 0)
        return res



# @lc code=end
