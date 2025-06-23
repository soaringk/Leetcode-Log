#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        charset = set()
        left = 0
        ans = 0
        for right, x in enumerate(s):
            while x in charset:
                charset.remove(s[left])
                left += 1
            charset.add(x)
            ans = max(ans, right - left + 1)
        return ans
    
    def myLengthOfLongestSubstring(self, s: str) -> int:
        ls = ''
        l = 0
        for c in s:
            if c in ls:
                if len(ls) > l:
                    l = len(ls)
                ls = ls[ls.index(c) + 1:]
            ls += c
        if len(ls) > l:
            l = len(ls)
        return l

    def otherlengthOfLongestSubstring(self, s: str) -> int:
        window = {}

        l = r = 0
        res = 0
        while (r < len(s)):
            c = s[r]  # 移入窗口的字符
            r += 1  # 右移

            # 进行窗口内数据的一系列更新
            window[c] = window.get(c, 0) + 1

            # 判断左侧窗口是否要收缩
            while window[c] > 1:
                d = s[l]  # 将移出窗口的字符
                l += 1  # 左移窗口
                # 进行窗口内数据的一系列更新
                window[d] -= 1

            res = max(res, r - l)

        return res


# @lc code=end
