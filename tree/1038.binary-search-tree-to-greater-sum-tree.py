#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s = 0

        def traverse(root):
            if root == None: return None

            traverse(root.right)

            nonlocal s
            s += root.val
            root.val = s

            traverse(root.left)

        traverse(root)
        return root

# @lc code=end
