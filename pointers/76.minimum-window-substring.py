#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#


# @lc code=start
class Solution:
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
