#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0: return None

        max_val = max(nums)
        max_idx = nums.index(max_val)

        left = self.constructMaximumBinaryTree(nums[:max_idx])
        right = self.constructMaximumBinaryTree(nums[max_idx + 1:])

        root = TreeNode(max_val, left, right)

        return root


# @lc code=end
