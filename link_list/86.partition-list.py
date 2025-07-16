#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 维护两个链表 small 和 large ，遍历完后拼起来
        # 因为是链表而不是数组，构建子链不增加空间复杂度。勇敢地构造子链即可，无需考虑节点交换。
        smallDummy, largeDummy = ListNode(), ListNode()

        small, large = smallDummy, largeDummy
        cur = head
        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next
            else:
                large.next = cur
                large = large.next
            cur = cur.next
        large.next = None # 清理干净，把它作为最后一个节点
        small.next = largeDummy.next # 拼起来

        return smallDummy.next
# @lc code=end

