package leetcode

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func widthOfBinaryTree(root *TreeNode) int {
	type pair struct {
		node  *TreeNode
		index int
	}
	ans := 1
	var array []pair = []pair{{root, 1}}
	for array != nil {
		last, first := array[len(array)-1], array[0]
		ans = max(ans, last.index-first.index+1)
		tmp := array
		array = nil
		for _, p := range tmp {
			if p.node.Left != nil {
				array = append(array, pair{p.node.Left, p.index * 2})
			}
			if p.node.Right != nil {
				array = append(array, pair{p.node.Right, p.index*2 + 1})
			}
		}
	}

	return ans
}
