#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while root or stack: # 还有节点，栈不为空
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def inorderTraversalRecursive(self, root: TreeNode) -> List[int]:
        l = []

        def traverse(root, l):
            if root == None: return

            traverse(root.left, l)
            l.append(root.val)
            traverse(root.right, l)

        traverse(root, l)

        return l


# @lc code=end
