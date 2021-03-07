#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p_a = headA
        p_b = headB

        while p_a != p_b:
            p_a = headB if p_a is None else p_a.next
            p_b = headA if p_b is None else p_b.next

        return p_a


# @lc code=end
