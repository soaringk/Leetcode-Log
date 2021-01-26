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

# @lc code=end
