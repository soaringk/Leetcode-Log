package leetcode

func trap(height []int) int {
	n := len(height)
	if n == 0 {
		return 0
	}

	var (
		leftMax  = make([]int, n)
		rightMax = make([]int, n)
	)
	leftMax[0] = height[0]
	rightMax[n-1] = height[n-1]
	// 正向遍历每个位置左边的最高柱子
	for i := 1; i < n; i++ {
		leftMax[i] = max(leftMax[i-1], height[i])
	}
	// 反向遍历每个位置右边的最高柱子
	for i := n - 2; i >= 0; i-- {
		rightMax[i] = max(rightMax[i+1], height[i])
	}

	// 计算雨水面积，每一列的高度 == min(左最高，右最高) - height[i]
	res := 0
	for i := 0; i < n; i++ {
		res += min(leftMax[i], rightMax[i]) - height[i]
	}
	return res
}
