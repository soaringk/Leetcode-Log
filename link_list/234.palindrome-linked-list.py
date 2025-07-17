#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# 树

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    left = None

    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head
        return self.traverse(head)

    def traverse(self, right):
        if right == None: return True
        res = self.traverse(right.next)

        res = res and (right.val == self.left.val)
        self.left = self.left.next
        return res

    # 876. 链表的中间结点
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 206. 反转链表
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome2(self, head: ListNode) -> bool:
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        while head2:
            if head.val != head2.val:  # 不是回文链表
                return False
            head = head.next
            head2 = head2.next
        return True
# @lc code=end
