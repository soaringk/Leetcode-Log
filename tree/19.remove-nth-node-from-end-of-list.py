#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# 树

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        while n > 0:
            fast = fast.next
            n -= 1
        if fast == None:
            return head.next
        while fast != None and fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

# @lc code=end
