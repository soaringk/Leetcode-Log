#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        curr = head
        prev = dummy

        while curr != None and curr.next != None:
            next = curr.next
            prev.next = next
            curr.next = next.next
            next.next = curr
            prev = curr
            curr = curr.next
        return dummy.next

# @lc code=end
