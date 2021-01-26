#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# 树

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    serial = ''

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def traverse(node, result):
            if node == None:
                self.serial += '#,'
                return None

            self.serial += str(node.val) + ','

            traverse(node.left, result)
            traverse(node.right, result)

        traverse(root, self.serial)
        return self.serial

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')

        def traverse(nodes):
            if len(nodes) == 0: return None

            first = nodes.pop(0)
            if first == '#': return None
            root = TreeNode(int(first))

            root.left = traverse(nodes)
            root.right = traverse(nodes)

            return root

        return traverse(nodes)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
