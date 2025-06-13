#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# 树


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        p0 = dummy = ListNode(next=head)
        # 找到要反转部分的上一个节点
        for _ in range(left - 1):
            p0 = p0.next

        # 反转链表
        pre = None
        cur = p0.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt 
        
        # 翻转链表的终止态：cur 为原链表尾部的下一个节点（剩余链表的头部），pre 为原链表的尾部
        # 利用这个性质将翻转后的链表接回原链表，
        # p0.next 指向原链表的头部，也是翻转后的尾部，要修改其 next 指向剩余链表，然后再让 p0.next 指向正确的翻转后的头部
        p0.next.next = cur
        p0.next = pre
        return dummy.next



# @lc code=end
