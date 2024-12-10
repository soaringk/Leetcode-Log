package leetcode

// twoSum TODO
// 1. 两数之和
// hash
func twoSum(nums []int, target int) []int {
	records := map[int]int{} // k = value, v = index
	for j, x := range nums {
		if i, ok := records[target-x]; ok {
			return []int{i, j}
		}
		records[x] = j
	}
	return nil
}
