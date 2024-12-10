package leetcode

// findLength TODO
// 718. 最长重复子数组
// dp
// 动态转移方程：D[i][j] = 0/D[i-1][j-1]+1
func findLength(nums1 []int, nums2 []int) int {
	n, m := len(nums1), len(nums2)
	D := make([][]int, n+1)
	for i := range D {
		D[i] = make([]int, m+1)
	}

	result := 0
	for i := 1; i < n+1; i++ {
		for j := 1; j < m+1; j++ {
			if nums1[i-1] == nums2[j-1] {
				D[i][j] = D[i-1][j-1] + 1
			} else {
				D[i][j] = 0
			}
			if result < D[i][j] {
				result = D[i][j]
			}
		}
	}
	return result
}
