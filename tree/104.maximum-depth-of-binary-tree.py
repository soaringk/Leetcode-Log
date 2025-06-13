#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node): # 返回该 node 为起点的最大深度
            if node == None:
                return 0
            return max(dfs(node.left), dfs(node.right)) + 1
        return dfs(root)
        
# @lc code=end

