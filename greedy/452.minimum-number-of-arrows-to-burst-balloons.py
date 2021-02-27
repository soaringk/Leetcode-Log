#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#


# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0
        points_sorted = sorted(points, key=lambda x: x[1])
        cnt = 1

        end = points_sorted[0][1]
        for s, e in points_sorted:
            if s > end:
                cnt += 1
                end = e

        return cnt

# @lc code=end
