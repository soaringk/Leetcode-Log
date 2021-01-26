#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def build(preorder, pre_start, pre_end, inorder, in_start, in_end):
            if pre_start > pre_end: return None

            root_val = preorder[pre_start]  # 前序获得跟节点
            root_idx = inorder.index(root_val)

            left_size = root_idx - in_start

            left = build(preorder, pre_start + 1, pre_start + left_size,
                         inorder, in_start, root_idx - 1)
            right = build(preorder, pre_start + left_size + 1, pre_end, inorder, root_idx + 1, in_end)

            root = TreeNode(root_val, left, right)

            return root

        return build(preorder, 0,
                     len(preorder) - 1, inorder, 0,
                     len(inorder) - 1)


# @lc code=end
