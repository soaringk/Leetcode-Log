package leetcode

func reverseKGroup(head *ListNode, k int) *ListNode {
	dummy := &ListNode{Next: head}
	var (
		prev = dummy // 子链表的前驱结点
		end  = dummy // 子链表的尾结点
	)
	for end.Next != nil {
		// 找到末尾
		for i := 0; i < k && end != nil; i++ {
			end = end.Next
		}
		if end == nil {
			break
		}

		var (
			start = prev.Next // 当前组头
			next  = end.Next  // 下一组头
		)
		end.Next = nil // 截断，让链表反转正常工作
		// 子组翻转链表
		prev.Next = reverseList(start)

		// 组反转后的首尾连接到正确的地方
		start.Next = next // start 反转后变成组的最后一个节点，连接到下一个组头
		prev = start      // 更新：prev 移动至下一组头的前一个节点
		end = prev        // 更新：end 与 prev 位置相同
	}
	return dummy.Next
}
