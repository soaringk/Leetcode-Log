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

ListNode.__lt__ = lambda a, b: a.val < b.val  # 让堆可以比较节点大小


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
        dummy = cur = ListNode(0) # 哨兵节点，作为合并后链表头节点的前一个节点
        q = PriorityQueue()
        for head in lists: # 把所有非空链表的头节点入堆
            if head:
                q.put(head)
        while not q.empty(): # 循环直到堆为空
            head = q.get() # 剩余节点中的最小节点
            cur.next = head # 把 node 添加到新链表的末尾
            cur = cur.next
            if head.next: # 下一个节点不为空
                q.put(head.next)
        return dummy.next

# @lc code=end
