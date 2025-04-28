#
# @lc app=leetcode id=2187 lang=python3
#
# [2187] Minimum Time to Complete Trips
#

# @lc code=start
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = min(time)
        right = totalTrips * min(time)
        while left <= right:
            mid = left + (right - left) // 2
            s = sum([mid // x for x in time]) # mid 时间，每个 bus 能完成的趟数数组
            if s >= totalTrips:
                right = mid - 1
            else:
                left = mid + 1
        return right + 1

# @lc code=end
