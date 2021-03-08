#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# 树


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

    def reverseListIterate(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        # reverse first node and prepare for the rest: 1->2->3->4->null
        prev = head.next  # 1->[2]->3->4->null
        next = head.next.next  # 1->2->[3]->4->null
        head.next.next = head  # 1<-2->3->4->null
        head.next = None  # null<-1<-2->3->4->null

        while next != None:
            tmp_next = next.next
            tmp_prev = next
            next.next = prev
            prev = tmp_prev
            next = tmp_next

        return prev

    def reverseListIterate2(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        nxt = head
        while cur != None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


# @lc code=end
