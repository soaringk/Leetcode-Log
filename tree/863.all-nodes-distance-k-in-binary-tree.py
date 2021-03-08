#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if root == None:
            return None
        res = []
        node_parent = {}
        visited = set()


        def traverse(root, node_parent):
            if root == None:
                return None
            if root.left:
                node_parent[root.left] = root
            if root.right:
                node_parent[root.right] = root
            traverse(root.left, node_parent)
            traverse(root.right, node_parent)

        def findResult(node, K, node_parent, visited, res):
            if node in visited:
                return
            visited.add(node)
            if K == 0:
                res.append(node.val)
                return
            if node.left:
                findResult(node.left, K - 1, node_parent, visited, res)
            if node.right:
                findResult(node.right, K - 1, node_parent, visited, res)
            if node in node_parent:
                findResult(node_parent[node], K - 1, node_parent, visited, res)

        traverse(root, node_parent)
        findResult(target, K, node_parent, visited, res)
        return res

# @lc code=end
