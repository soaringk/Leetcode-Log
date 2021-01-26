#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# 树


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = 0
        rank = 0

        def traverse(node: TreeNode, k: int):
            if node == None: return

            traverse(node.left, k)
            nonlocal rank
            rank += 1
            if k == rank:
                nonlocal res
                res = node.val
                return
            traverse(node.right, k)

        traverse(root, k)
        return res


# @lc code=end
