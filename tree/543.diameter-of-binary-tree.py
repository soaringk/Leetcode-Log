#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 遍历最长链的时候顺便计算直径
    # 在当前节点拐弯的直径长度 = 左最长链 + 右最长链 + 2
    # 但是因为递归函数是在遍历最长链，所以 return 的内容是max(左最长链, 右最长j) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            if node is None:
                return -1
            l_len = dfs(node.left)
            r_len = dfs(node.right)
            nonlocal ans
            ans = max(ans, l_len + r_len + 2)
            return max(l_len, r_len) + 1
        dfs(root)
        return ans
        
# @lc code=end

