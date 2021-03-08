#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = []
        cnt = 1

        if root:
            queue.append(root)

        while queue:
            level = []
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if cnt % 2 == 1:
                res.append(level)
            else:
                level.reverse()
                res.append(level)
            cnt += 1

        return res

# @lc code=end
