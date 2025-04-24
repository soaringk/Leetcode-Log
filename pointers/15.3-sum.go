package leetcode

import "sort"

// 排序+双指针
func threeSum(nums []int) [][]int {
	n := len(nums)
	sort.Ints(nums)
	ans := make([][]int, 0)

	// 固定一个 a
	for first := 0; first < n; first++ {
		if first > 0 && nums[first] == nums[first-1] { // 规避重复
			continue
		}
		third := n - 1 // c 在最右端
		target := -1 * nums[first]
		// 枚举 b、c，分别位于寻找范围的两侧
		for second := first + 1; second < n; second++ {
			if second > first+1 && nums[second] == nums[second-1] { // 规避重复
				continue
			}

			// b 在 c 的左边，找目标
			for second < third && nums[second]+nums[third] > target {
				third--
			}
			if second == third {
				break // 没找到
			}
			if nums[second]+nums[third] == target {
				ans = append(ans, []int{nums[first], nums[second], nums[third]})
			}
		}
	}
	return ans
}
