#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start
class LFUCache:

    def __init__(self, capacity: int):
        self.k2val = {}
        self.k2freq = {}
        self.freq2k = {}
        self.min_freq = 0
        self.capacity = capacity


    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
