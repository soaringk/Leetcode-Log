package leetcode

// TreeNode TODO
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// levelOrder TODO
// 102. 二叉树层次遍历
func levelOrder(root *TreeNode) [][]int {
	ret := [][]int{}
	if root == nil {
		return ret
	}
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
		for i := 0; i < len(layer)/2; i++ {
			layer[i], layer[len(layer)-i-1] = layer[len(layer)-i-1], layer[i]
		}
		ret = append(ret, layer)
		queue = queue[n:]
	}
	return ret
}
