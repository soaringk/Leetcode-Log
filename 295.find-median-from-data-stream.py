#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large = []
        self.small = []


    def addNum(self, num: int) -> None:
        if len(self.large) <= len(self.small):
            max_small = heapq.heappushpop(self.small, -num)
            heapq.heappush(self.large, -max_small)
        else:
            min_large = heapq.heappushpop(self.large, num)
            heapq.heappush(self.small, -min_large)


    def findMedian(self) -> float:
        if len(self.large) < len(self.small):
            return self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] - self.small[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
obj = MedianFinder()
obj.addNum(-1)
param_1 = obj.findMedian()
obj.addNum(-2)
param_1_5 = obj.findMedian()
obj.addNum(-3)
param_2 = obj.findMedian()
obj.addNum(-4)
param_2_5 = obj.findMedian()
obj.addNum(-5)
param_3 = obj.findMedian()
