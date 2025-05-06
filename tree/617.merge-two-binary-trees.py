#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> Optional[TreeNode]:
            if node1 == None and node2 == None:
                return None
            elif node1 and node2:
                node = TreeNode(node1.val + node2.val)  
                node.left = dfs(node1.left, node2.left)
                node.right = dfs(node1.right, node2.right)
            elif node1:
                node = TreeNode(node1.val)
                node.left = dfs(node1.left, None)
                node.right = dfs(node1.right, None)
            elif node2:
                node = TreeNode(node2.val)
                node.left = dfs(None, node2.left)
                node.right = dfs(None, node2.right)
            return node
        return dfs(root1, root2)

    # 搞清楚 mergeTrees 函数的定义：将两个数合并，然后返回这个数的父节点。可以直接利用这个性质递归
    # 1. root1 空，直接返回 root2，直接继承所有子树；
    # 2. root2 空，直接返回 root1，直接继承所有子树；
    # 3. 都不为空，只操作当前节点，用函数定义递归处理左右子树
    def mergeTreesSimpler(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None: return root2
        if root2 is None: return root1
        return TreeNode(root1.val + root2.val,
            self.mergeTrees(root1.left, root2.left),    # 合并左子树
            self.mergeTrees(root1.right, root2.right))  # 合并右子树

# @lc code=end

