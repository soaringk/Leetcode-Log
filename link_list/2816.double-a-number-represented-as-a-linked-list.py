#
# @lc app=leetcode id=2816 lang=python3
#
# [2816] Double a Number Represented as a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if head.val > 4:
            head = ListNode(1, head)
        while cur:
            cur.val = (cur.val * 2) % 10
            if cur.next and cur.next.val > 4:
                # 因为是自身乘2，所以绝对不会出现连续 carry 进位的情况，所以可以顺序遍历。任意数组相加时不能这么做
                cur.val = (cur.val + 1) % 10
            cur = cur.next
        return head


# @lc code=end
