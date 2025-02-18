package leetcode

func maxArea(height []int) int {
	if len(height) < 2 {
		return 0
	}
	var area int
	// 双指针，每次移动较小的指针
	// 因此面积取决于较小的高度，如果移动较大的指针，面积也不可能超过当前的值
	for l, r := 0, len(height)-1; l < r; {
		h := min(height[l], height[r])
		w := r - l
		area = max(area, h*w)
		if height[l] > height[r] {
			r--
		} else {
			l++
		}
	}
	return area
}
