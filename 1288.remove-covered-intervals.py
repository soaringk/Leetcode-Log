#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 起点升序排列，起点相同时降序排列
        intervals.sort(key=lambda x: (x[0], -x[1]))

        # 记录合并区间的起点和终点
        left = intervals[0][0]
        right = intervals[0][1]

        res = 0
        for intv in intervals[1:]:
            if left <= intv[0] and right >= intv[1]:
                res += 1
            elif right >= intv[0] and right <= intv[1]:  # 合并
                right = intv[1]
            elif right < intv[0]:
                left = intv[0]
                right = intv[1]

        return len(intervals) - res


# @lc code=end
