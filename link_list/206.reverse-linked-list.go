package leetcode

func reverseList(head *ListNode) *ListNode {
	var pre, curr *ListNode
	curr = head
	pre = nil
	for curr != nil {
		tmp := curr.Next
		curr.Next = pre
		pre = curr
		curr = tmp
	}
	return pre
}
