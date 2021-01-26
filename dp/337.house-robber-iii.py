#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        dp = {}

        def traverse(root, dp):
            if root == None: return 0
            if root in dp: return dp[root]

            do_rob = root.val
            if root.left != None:
                do_rob = do_rob + traverse(root.left.left, dp) + traverse(root.left.right, dp)
            if root.right != None:
                do_rob = do_rob + traverse(root.right.left, dp) + traverse(root.right.right, dp)

            not_rob = traverse(root.left, dp) + traverse(root.right, dp)

            res = max(do_rob, not_rob)
            dp[root] = res

            return res

        res = traverse(root, dp)

        return res
# @lc code=end
