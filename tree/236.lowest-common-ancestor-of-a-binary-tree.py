#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# 树

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        描述：给该函数输入三个参数root，p，q，它会返回一个节点。
        情况 1，如果p和q都在以root为根的树中，函数返回的即使p和q的最近公共祖先节点。
        情况 2，那如果p和q都不在以root为根的树中怎么办呢？函数理所当然地返回null呗。
        情况 3，那如果p和q只有一个存在于root为根的树中呢？函数就会返回那个节点。
        """
        def traverse(root, p, q):
            # base case
            if root == None: return
            if root == p or root == q: return root

            left = traverse(root.left, p, q)
            right = traverse(root.right, p, q)

            # 1.
            if left != None and right != None:
                return root
            # 2.
            if left == None and right == None:
                return None
            # 3.
            if left == None and right != None:
                return right
            elif right == None and left != None:
                return left
            # return left if right == None else right

        node = traverse(root, p, q)

        return node
# @lc code=end
