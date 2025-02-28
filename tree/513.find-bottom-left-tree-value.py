#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (71.57%)
# Likes:    3867
# Dislikes: 298
# Total Accepted:    391.3K
# Total Submissions: 546.7K
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, return the leftmost value in the last row of
# the tree.
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: 1
#
#
# Example 2:
#
#
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # 从右进行层序遍历的最后一个节点
        q = deque([root])
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val
# @lc code=end
