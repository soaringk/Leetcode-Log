#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
from collections import Counter


# @lc code=start
class Solution:
    def minWindowConsice(self, s: str, t: str) -> str:
        ans_left, ans_right = -1, len(s)
        cnt_s = Counter()  # s 子串字母的出现次数
        cnt_t = Counter(t)  # t 中字母的出现次数

        left = 0
        for right, c in enumerate(s):  # 移动子串右端点
            cnt_s[c] += 1  # 右端点字母移入子串
            while cnt_s >= cnt_t:  # 涵盖
                if right - left < ans_right - ans_left:  # 找到更短的子串
                    ans_left, ans_right = left, right  # 记录此时的左右端点
                cnt_s[s[left]] -= 1  # 左端点字母移出子串
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]

    def minWindow(self, s: str, t: str) -> str:
        need = {}; window = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        l = r = valid = 0
        # 记录最小覆盖子串的起始索引及长度
        start = 0
        length = float("inf")
        while (r < len(s)):
            c = s[r]  # 移入窗口的字符
            r += 1  # 右移

            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while valid == len(need):
                # 在这里更新最小覆盖子串
                if r - l < length:
                    start = l
                    length = r - l
                d = s[l]  # 将移出窗口的字符
                l += 1  # 左移窗口
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if length == float("inf") else s[start:start + length]


# @lc code=end
