#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(norder, in_start, in_end, postorder, post_start, post_end):
            if in_start > in_end: return None

            root_val = postorder[post_end]
            root_idx = inorder.index(root_val)

            left_size = root_idx - in_start

            left = build(inorder, in_start, root_idx - 1, postorder, post_start, post_start + left_size - 1)
            right = build(inorder, root_idx + 1, in_end,
                          postorder, post_start + left_size, post_end - 1)

            root = TreeNode(root_val, left, right)

            return root

        return build(inorder, 0,
                     len(inorder) - 1, postorder, 0,
                     len(postorder) - 1)


# @lc code=end
