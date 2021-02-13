#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    def intervalIntersetion(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0

        res = []
        while i < len(firstList) and j < len(secondList):
            a1, a2 = firstList[i]
            b1, b2 = secondList[j]
            if a2 >= b1 and b2 >= a1:
                res.append([max(a1, b1), min(a2, b2)])
            if b2 < a2:
                j += 1
            else:
                i += 1

        return res

# @lc code=end
