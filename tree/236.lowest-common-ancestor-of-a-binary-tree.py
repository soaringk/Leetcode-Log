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
        情况 1，当 left 和 right 同时不为空，说明 p,q 分列在 root 的左右子树，因此 root 为最近公共祖先，返回 root
        情况 2，当 left 和 right 同时为空，说明 root 的左右子树都不包括 p,q 节点，返回空
        情况 3，那如果p和q只有一个存在于root为根的树中呢？函数就会返回那个节点。
        """
        def traverse(root, p, q):
            # base case
            if root == None: return None
            if root == p or root == q: return root

            left = traverse(root.left, p, q)
            right = traverse(root.right, p, q)

            # 1.
            if left and right:
                return root
            # 2.
            if left == None and right == None:
                return None
            # 3.
            return left if right == None else right

        node = traverse(root, p, q)

        return node
# @lc code=end
