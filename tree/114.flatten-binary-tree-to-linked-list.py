#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None: return

        self.flatten(root.left)
        self.flatten(root.right)

        # 后序遍历
        left = root.left
        right = root.right

        root.right = left
        root.left = None

        p = root
        while p.right != None:
            p = p.right
        p.right = right

# @lc code=end
