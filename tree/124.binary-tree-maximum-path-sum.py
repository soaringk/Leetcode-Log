#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        计算一个节点的最大贡献值并返回
        1. 空节点的最大贡献值等于0
        2. 非空节点的最大贡献值等于节点值与其子节点中的较大贡献值之和（对于叶节点而言，最大贡献值等于节点值）
        """
        max_path = float('-inf')

        def max_gain(node):
            if not node:
                return 0

            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            nonlocal max_path
            max_path = max(max_path, node.val + left_gain + right_gain)

            return node.val + max(left_gain, right_gain)

        max_gain(root)

        return max_path

# @lc code=end
