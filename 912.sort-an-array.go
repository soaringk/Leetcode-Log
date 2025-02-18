package leetcode

import "math/rand"

func sortArray(nums []int) []int {
	quick_sort(nums, 0, len(nums)-1)
	return nums
}

func quick_sort(nums []int, l, r int) {
	var partition = func(nums []int, l, r int) int {
		randIdx := rand.Intn(r-l+1) + l
		pivot := nums[randIdx]
		nums[r], nums[randIdx] = nums[randIdx], nums[r]
		i := l
		for j := l; j < r; j++ {
			if nums[j] <= pivot {
				nums[i], nums[j] = nums[j], nums[i]
				i++
			}
		}
		nums[i], nums[r] = nums[r], nums[i]
		return i
	}

	if l < r {
		pos := partition(nums, l, r)
		quick_sort(nums, l, pos-1)
		quick_sort(nums, pos+1, r)
	}
}
