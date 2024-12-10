package leetcode

// zigzagLevelOrder TODO
// 103. 二叉树的锯齿形层次遍历
func zigzagLevelOrder(root *TreeNode) [][]int {
	ret := [][]int{}
	if root == nil {
		return ret
	}
	inverted := false
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		n := len(queue)
		var layer []int
		for j := 0; j < n; j++ {
			node := queue[j]
			layer = append(layer, node.Val)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		if inverted {
			for i := 0; i < len(layer)/2; i++ {
				layer[i], layer[len(layer)-i-1] = layer[len(layer)-i-1], layer[i]
			}
		}
		inverted = !inverted
		ret = append(ret, layer)
		queue = queue[n:]
	}
	return ret
}
