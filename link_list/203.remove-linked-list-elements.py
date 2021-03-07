#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre = None
        cur = head

        while cur != None:
            if cur.next and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
        return head


# @lc code=end
