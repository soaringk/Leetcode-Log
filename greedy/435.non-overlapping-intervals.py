#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0: return 0
        sort_intervals = sorted(intervals, key = lambda x: x[1])
        cnt = 1

        start = sort_intervals[0][0]
        end = sort_intervals[0][1]
        for s, e in sort_intervals:
            if s >= end:
                cnt += 1
                end = e

        return len(intervals) - cnt


# @lc code=end
