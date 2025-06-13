# 原则

## 翻转链表链表

1. 需要三个变量 pre, cur, next, 分别指向当前处理节点的上一个节点、当前节点、当初节点的下一个
2. 开始条件：cur 赋值为要翻转部分的头节点 head。如果要访问 pre.next 而 pre 可能为空，可以用一个 dummy
3. 结束条件：翻转结束后，pre 指向原链表的尾部，cur 指向原链表的下一个节点

# 模版
#206 翻转链表
```python
def reverseList(self, head: ListNode) -> ListNode:
    pre = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre
```
