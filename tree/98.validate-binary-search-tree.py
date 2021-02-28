#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def traverse(root, minimum, maximum):
            if root == None:
                return True

            if minimum and not minimum.val < root.val:
                return False
            if maximum and not maximum.val > root.val:
                return False

            left_res = traverse(root.left, minimum, root)
            right_res = traverse(root.right, root, maximum)

            return left_res and right_res

        return traverse(root, None, None)
# @lc code=end
