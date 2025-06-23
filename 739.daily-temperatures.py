#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 从右往左的单调栈，数字从顶部是从小到大排列
        n = len(temperatures)
        ans = [0] * n
        # 从右往左遍历，如果当前数字比栈顶大，那么需要一直出栈，然后就找到了目标
        # 完成步骤之后，将当前元素加入栈。之前出队的小值就都可以废弃掉了（想象成山，前面的数字看不到两座山峰之间的低谷，不需要关注）
        stack = [] # 记录的是气温的下标
        for i in range(n-1, -1, -1):
            t = temperatures[i]
            while stack and t >= temperatures[stack[-1]]: # 与栈顶气温做比较
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans

    def dailyTemporaturesLeftRight(self, temperatures: List[int]) -> List[int]:
        # 单调栈：及时去掉无用数据，保证栈中数据有序
        # 单调栈数字从顶部是从小到大排列
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n):
            t = temperatures[i]
            while st and t > temperatures[st[-1]]:
                j = st.pop()
                ans[j] = i - j
            st.append(i)
        return ans
# @lc code=end

