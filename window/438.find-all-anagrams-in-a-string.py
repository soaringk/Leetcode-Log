#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {}
        window = {}
        for c in p:
            need[c] = need.get(c, 0) + 1

        l = r = valid = 0
        res = []
        while (r < len(s)):
            c = s[r]  # 移入窗口的字符
            r += 1  # 右移

            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while r - l >= len(p):
                # 在这里更新最小覆盖子串
                if valid == len(need):
                    res.append(l)
                d = s[l]  # 将移出窗口的字符
                l += 1  # 左移窗口
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return res
# @lc code=end
