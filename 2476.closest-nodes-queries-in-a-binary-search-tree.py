#
# @lc app=leetcode id=2476 lang=python3
#
# [2476] Closest Nodes Queries in a Binary Search Tree
#
from bisect import bisect_left

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 可以通过一次中序遍历 得到有一个严格递增数组 a，
    # 再在 a 上做二分查找，就可以做到单次询问 O(logn) 的时间了。
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        a = []
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs(node.left)
            a.append(node.val)
            dfs(node.right)
        dfs(root)

        n = len(a)
        ans = []
        for q in queries:
            j = bisect_left(a, q)
            mx = a[j] if j < n else -1
            if j == n or a[j] != q:  # a[j]>q, a[j-1]<q
                j -= 1
            mn = a[j] if j >= 0 else -1
            ans.append([mn, mx])
        return ans

# @lc code=end

