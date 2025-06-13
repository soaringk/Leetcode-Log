#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 设 head 到入环口（答案）需要走 a 步，环长为 c 步
        # 设相遇时慢指针走了 b 步，那么快指针走了 2b 步，由于快指针可能多走了 k 圈，因此以相对速度计算：2b - b = kc
        #
        # 接下来注意到，慢指针从入环口开始，在环中走了 b - a = kc - a 步
        # 又注意到 (kc - a) + a = kc，因此两个指针再走 a 步就会到达入环口
        # 而 a 又是 head 到入环口的距离，因此让 head 和慢/快指针都再走 a 步就能到达入环口
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow
        return None


# @lc code=end
