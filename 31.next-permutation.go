package leetcode

func nextPermutation(nums []int) {
	if len(nums) <= 1 {
		return
	}

	// i: [0, length-1]，实际可以少扫描一个，所以是 length-2
	// j: [i+1, length-1]
	// k: [j, length-1]
	i, j, k := len(nums)-2, len(nums)-1, len(nums)-1

	// find: A[i]<A[j], backwards
	for i >= 0 && nums[i] >= nums[j] {
		i--
		j--
	}

	if i >= 0 {
		// find: A[i]<A[k]
		for nums[i] >= nums[k] {
			k--
		}
		nums[i], nums[k] = nums[k], nums[i]
	}

	// reverse
	for start, end := j, len(nums)-1; start < end; start, end = start+1, end-1 {
		nums[start], nums[end] = nums[end], nums[start]
	}
}
