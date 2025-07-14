#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        st = set(nums)  # 把 nums 转成哈希集合
        for x in st:  # 遍历哈希集合。遍历 nums 的做法会导致每个 1 都跑一个 O(n) 的循环，总的循环次数是 O(n^2)，会超时。
            if x - 1 in st: # 如果有更小的，直接遍历更小的，节约时间
                continue
            # x 是序列的起点
            y = x + 1
            while y in st:  # 不断查找下一个数是否在哈希集合中
                y += 1
            # 循环结束后，y-1 是最后一个在哈希集合中的数
            ans = max(ans, y - x)
        return ans
# @lc code=end
