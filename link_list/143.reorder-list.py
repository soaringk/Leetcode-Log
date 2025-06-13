#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
'''
1.找到原链表的中点 876
2.将原链表的右半端反转 206
3.将原链表的两端合并 21
'''

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return

        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None

        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)

    def middleNode(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def mergeList(self, l1, l2):
        while l1 and l2:
            nxt1 = l1.next
            nxt2 = l2.next

            l1.next = l2
            l2.next = nxt1

            l1 = nxt1
            l2 = nxt2


# @lc code=end
