package leetcode

func mergeKLists(lists []*ListNode) *ListNode {
	// 1.遍历K，可以用最小堆加速

	// 2.分治
	return merge(lists, 0, len(lists)-1)
}

func merge(lists []*ListNode, l, r int) *ListNode {
	if l == r {
		return lists[l]
	}
	if l > r {
		return nil
	}
	mid := (l + r) / 2
	return mergeTowList(merge(lists, l, mid), merge(lists, mid+1, r))
}

func mergeTowList(a, b *ListNode) *ListNode {
	if a == nil {
		return b
	}
	if b == nil {
		return a
	}
	dummy := &ListNode{}
	curr := dummy
	for a != nil && b != nil {
		if a.Val < b.Val {
			curr.Next = a
			a = a.Next
		} else {
			curr.Next = b
			b = b.Next
		}
		curr = curr.Next
	}
	if a != nil {
		curr.Next = a
	} else if b != nil {
		curr.Next = b
	}
	return dummy.Next
}
