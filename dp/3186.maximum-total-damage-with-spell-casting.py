#
# @lc app=leetcode id=3186 lang=python3
#
# [3186] Maximum Total Damage With Spell Casting
#
from typing import List
from collections import Counter

# @lc code=start
class Solution:
    # 与 740 一样，本处采用另一种 O(nlogn) 的写法
    def maximumTotalDamage(self, power: List[int]) -> int:
        # 方便起见，将 nums 转化成一个 counter，方便后续取值。当然，循环检查是否相等然后累加也是做得到的，for 循环会麻烦一些
        cnt = Counter(power)
        a = sorted(cnt.keys())
        n = len(a)
        dp = [0] * (n + 1)
        j = 0
        for i in range(n):
            x = a[i]
            while a[j] < x - 2:
                j += 1
            dp[i + 1] = max(dp[i], dp[j] + x * cnt[x])
        return dp[-1]


# @lc code=end
Solution().maximumTotalDamage([1,1,3,4])
