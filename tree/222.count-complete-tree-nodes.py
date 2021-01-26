#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
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
    def countNodes(self, root: TreeNode) -> int:
        def traverse(root):
            l = root
            r = root
            hl = 0
            hr = 0

            while l != None:
                l = l.left
                hl += 1

            while r != None:
                r = r.right
                hr += 1

            # 高度不同不计算
            if hl == hr:
                # print(2**hl - 1)
                return 2**hl - 1

            # 一棵完全二叉树的两棵子树，至少有一棵是满二叉树
            return 1 + traverse(root.left) + traverse(root.right)

        return traverse(root)

# @lc code=end
