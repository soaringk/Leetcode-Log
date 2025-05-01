#
# @lc app=leetcode id=2517 lang=python3
#
# [2517] Maximum Tastiness of Candy Basket
#
from typing import List

# @lc code=start
class Solution:
    # 「任意两种糖果价格绝对差的最小值」等价于「排序后，任意两种相邻糖果价格绝对差的最小值」。
    # 搜索范围 [0, max-min]
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def countWithDistance(d: int) -> int:
            cnt = 1
            pre = price[0]  # 先选一个最小的甜蜜度
            for p in price:
                if p >= pre + d:  # 可以选
                    cnt += 1
                    pre = p  # 上一个选的甜蜜度
            return cnt

        price.sort()
        left = 0
        right = (price[-1] - price[0]) // (k - 1)
        while left <= right:
            mid = left + (right - left) // 2
            if countWithDistance(mid) >= k: # 满足条件
                left = mid + 1
            else:
                right = mid - 1
        return right


# @lc code=end
Solution().maximumTastiness([13,5,1,8,21,2],3)
