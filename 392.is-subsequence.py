#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
from typing import List
# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        n, m = len(s), len(t)
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n

    def isSubsequenceBatch(self, s_list: List[str], t) -> bool:

        # preprocessing
        char_idx_map = {}
        for i, v in enumerate(t):
            char_idx_map.setdefault(v, []).append(i)

        def left_bound(idx_list, target):
            left, right = 0, len(idx_list)

            while left < right:
                mid = left + (right - left) // 2
                if idx_list[mid] >= target:
                    right = mid
                else:
                    left = mid + 1

            return left

        res = []
        for s in s_list:
            if not s:   # empty string to match, default to True
                res.append(True)
                continue

            # start matching
            j = 0
            flag = True
            for c in s:
                if c not in char_idx_map:   # char missing
                    flag = False
                    break

                idx_list = char_idx_map[c]
                pos = left_bound(idx_list, j)

                # not found
                if pos == len(idx_list):
                    flag = False
                    break

                j = idx_list[pos] + 1

            res.append(flag)

        return res

# @lc code=end
s = Solution()
s.isSubsequenceBatch(["axc"], "ahbgdc")
