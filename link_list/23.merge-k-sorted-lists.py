#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
from queue import PriorityQueue
from itertools import count
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        if amount == 0: return None

        interval = 1

        def merge2Lists(l1, l2):
            dummy = cur = ListNode(-1)

            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next

            if l1:
                cur.next = l1
            if l2:
                cur.next = l2

            return dummy.next

        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]

    def mergeKListsHeap(self, lists: List[ListNode]) -> ListNode:
        dummy = cur = ListNode(0)
        q = PriorityQueue()
        index = count(0)
        for head in lists:
            if head:
                q.put((head.val, next(index), head))
        while not q.empty():
            val, _, head = q.get()
            cur.next = head

            cur = cur.next
            head = head.next
            if head:
                q.put((head.val, next(index), head))
        return dummy.next

# @lc code=end
