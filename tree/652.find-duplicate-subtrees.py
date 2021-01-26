#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
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
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        # 子树记录
        memo = {}
        # 重复的子树根节点
        res = []

        def traverse(root: TreeNode) -> str:
            if root == None: return '#'

            left = traverse(root.left)
            right = traverse(root.right)

            sub_tree = left + "," + right + "," + str(root.val)

            freq = memo.get(sub_tree, 0)

            if freq == 1:
                res.append(root)
            memo[sub_tree] = freq + 1

            return sub_tree

        traverse(root)
        return res
# @lc code=end
