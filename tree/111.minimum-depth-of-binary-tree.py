#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
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
    def minDepth(self, root: TreeNode) -> int:
        if root == None: return 0

        depth = 1
        q = [root]

        while len(q) != 0:
            for i in range(len(q)):
                cur = q.pop(0)
                if cur.left == None and cur.right == None:
                    return depth
                if cur.left != None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)

            depth += 1

        return depth

# @lc code=end
