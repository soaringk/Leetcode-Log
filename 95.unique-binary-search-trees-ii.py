#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def backtrack(start, end):
            if start > end:
                return [None, ]

            all_trees = []
            for i in range(start, end + 1):
                left = backtrack(start, i - 1)
                right = backtrack(i + 1, end)

                for l in left:
                    for r in right:
                        curr = TreeNode(i)
                        curr.left = l
                        curr.right = r
                        all_trees.append(curr)

            return all_trees

        return backtrack(1, n) if n else []


# @lc code=end
