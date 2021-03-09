#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = TreeNode(val)
        if not root:
            return node

        cur = root
        while cur:
            if val < cur.val and cur.left:
                cur = cur.left
            elif val < cur.val and not cur.left:
                cur.left = node
                return root
            elif val > cur.val and cur.right:
                cur = cur.right
            elif val > cur.val and not cur.right:
                cur.right = node
                return root
# @lc code=end
