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

successor = None
class Solution:

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1: return self.reverseN(head, n)

        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

    def reverseN(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
            successor = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = successor
        return last


# @lc code=end


S = Solution()
l = []
for i in range(1, 7):
    l.append(ListNode(i, ))
for i in range(len(l) - 1):
    prev = l[i]
    next = l[i + 1]
    prev.next = next
t = l[0]
while t.next != None:
    print(t.val)
    t = t.next
a = S.reverseBetween(l[0], 2, 4)
while a.next != None:
    print(a.val)
    a = a.next


class SolutionOfficial:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None

        left, right = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        recurseAndReverse(right, m, n)
        return head
