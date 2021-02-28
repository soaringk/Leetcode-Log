#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
from tree_helper import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        cur = root
        pre = None

        while cur:
            if cur.left:
                p = cur.left
                while p.right and p.right != cur:
                    p = p.right
                if not p.right:
                    p.right = cur
                    cur = cur.left
                    continue
                else:
                    p.right = None
            if pre and cur.val < pre.val:
                if not first:
                    first = pre
                second = cur
            pre = cur
            cur = cur.right

        first.val, second.val = second.val, first.val

# @lc code=end
s = Solution()
s.recoverTree(deserialize('[1,3,null,null,2]'))
