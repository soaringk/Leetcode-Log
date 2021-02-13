#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 起点升序排列，起点相同时降序排列
        intervals.sort(key=lambda x: (x[0], -x[1]))

        # 记录合并区间的起点和终点
        res = [intervals[0]]
        for intv in intervals[1:]:
            last = res[-1]
            if last[1] >= intv[0]:
                last[1] = max(last[1], intv[1])
            else:
                res.append(intv)
            # left, right = res.pop()
            # if left <= intv[0] and right >= intv[1]:
            #     res.append([left, right])
            # elif right >= intv[0] and right <= intv[1]:  # 合并
            #     right = intv[1]
            #     res.append([left, right])
            # elif right < intv[0]:
            #     res.append([left, right])
            #     left = intv[0]
            #     right = intv[1]
            #     res.append([left, right])

        return res
# @lc code=end
