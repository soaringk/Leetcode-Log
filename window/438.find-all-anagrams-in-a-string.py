#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
from collections import Counter
from typing import List

# @lc code=start
class Solution:
    # 常规不定长窗口
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        cnt = Counter(p)  # 统计 p 的每种字母的出现次数
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1  # 右端点字母进入窗口
            while cnt[c] < 0:  # 字母 c 太多了
                cnt[s[left]] += 1  # 左端点字母离开窗口
                left += 1
            if right - left + 1 == len(p):  # s' 和 p 的每种字母的出现次数都相同
                ans.append(left)  # s' 左端点下标加入答案
        return ans

    # 定长窗口 = len(p)
    # 维护长为 n 的子串 s′ 的每种字母的出现次数。如果 s′ 的每种字母的出现次数，和 p 的每种字母的出现次数都相同，那么 s′ 是 p 的异位词，把 s′ 左端点下标加入答案。
    def findAnagramsFixed(self, s: str, p: str) -> List[int]:
        ans = []
        cnt_p = Counter(p)  # 统计 p 的每种字母的出现次数
        cnt_s = Counter()  # 统计 s 的长为 len(p) 的子串 s' 的每种字母的出现次数
        for right, c in enumerate(s):
            cnt_s[c] += 1  # 右端点字母进入窗口
            left = right - len(p) + 1
            if left < 0:  # 窗口长度不足 len(p)
                continue
            if cnt_s == cnt_p:  # s' 和 p 的每种字母的出现次数都相同
                ans.append(left)  # s' 左端点下标加入答案
            cnt_s[s[left]] -= 1  # 左端点字母离开窗口
        return ans

# @lc code=end
