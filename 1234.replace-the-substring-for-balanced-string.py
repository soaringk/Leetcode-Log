#
# @lc app=leetcode id=1234 lang=python3
#
# [1234] Replace the Substring for Balanced String
#
'''
根据题意，如果在待替换子串之外的任意字符的出现次数超过 m = n/4，那么无论怎么替换，都无法使这个字符在整个字符串中的出现次数为 m。
反过来说，如果在待替换子串之外的任意字符的出现次数都不超过 m，那么可以通过替换，使 s 为平衡字符串，即每个字符的出现次数均为 m。
'''
from collections import Counter

# @lc code=start
class Solution:
    def balancedString(self, s: str) -> int:
        m = len(s) // 4 # 题目确保是 4 的倍数
        cnt = Counter(s) # 待替换子串之外的字符
        if len(cnt) == 4 and min(cnt.values()) == m:
            return 0

        ans, left = inf, 0 
        for right, x in enumerate(s): # 枚举右端点。此时子串之外肯定是不满足要求的，即子串之外的字符出现次数超过了 n/4
            cnt[x] -= 1 # 根据窗口修正"代替换子串之外的字符计数"
            while max(cnt.values()) <= m: # 窗口之外符合条件，可以开始计答案了。迭代直到窗口之外不符合条件
                # 窗口外的任意字符的出现次数都不超过 m，则说明从 left 到 right 的这段子串可以是待替换子串
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1
                left += 1  # 缩小子串
        return ans

        
# @lc code=end

