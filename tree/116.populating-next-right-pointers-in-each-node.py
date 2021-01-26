#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
# 树

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None: return None

        def connnectTwoNode(left, right):
            if left == None or right == None: return None

            # 传入的两个节点连接
            left.next = right

            ###
            # 将每一层二叉树节点连接起来
            connnectTwoNode(left.left, left.left)
            connnectTwoNode(right.left, right.left)
            ###
            # 将每两个相邻节点都连接起来
            connnectTwoNode(left.right, right.left)

        connnectTwoNode(root.left, root.right)
        return root


# @lc code=end
