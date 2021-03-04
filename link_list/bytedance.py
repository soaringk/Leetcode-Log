#coding=utf-8
# import sys
# 字节面试题：一个链表，基数位升序，偶数位降序，返回一个从小到大顺序排列的链表
# 思路：
# 1.分成奇偶两组链表
# 2.偶数组链表翻转
# 3.合并两个数组


def main(head):
    odd = head
    even = head.next
    odd_head = odd
    even_head = even

    # even/odd 分成两组链表
    while even != None and even.next != None:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = None

    # 翻转后的偶数链表
    p = reverseList(even_head)
    res = mergeList(odd_head, p)
    return res


def reverseListRecursive(p):
    if p.next == None:
        return p
    last = reverseList(p.next)
    p.next.next = p
    p.next = None
    return last

def reverseList(p):
    pre = None
    while p != None:
        tmp = p.next
        p.next = pre
        pre = p
        p = tmp
    return pre


def mergeList(odd, even):
    dummy_head = LinkNode(-1)
    prev = dummy_head

    while odd != None and even != None:
        if odd.val <= even.val:
            prev.next = odd
            odd = odd.next
        else:
            prev.next = even
            even = even.next
        prev = prev.next

    # 剩下的append
    if odd != None:
        prev.next = odd
    if even != None:
        prev.next = even

    return dummy_head.next


class LinkNode():

    next = None

    def __init__(self, val):
        self.val = val


def createLinkList():
    l = [1, 200, 10, 120, 30, 8, 88, 4]
    nodes = []
    for i in range(len(l)):
        nodes.append(LinkNode(l[i]))
    for i in range(len(l) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]


l = createLinkList()
res = main(l)
while res != None:
    print(res.val)
    res = res.next
