package leetcode

// lengthOfLongestSubstring 3. 最长无重复的子字符串
// 双指针
func lengthOfLongestSubstring(s string) int {
	// 双指针
	var (
		left    int
		right   int
		charset = map[byte]bool{}
		result  int
	)
	// 拓展右边界
	for right = 0; right < len(s); right++ {
		// 检查的元素
		char := s[right]
		// 区间[left,right]不符合题意：不断缩小左边界，直到能把右边界加入当前 set
		for charset[char] {
			// 缩短左边界
			delete(charset, s[left])
			left++
		}
		// 满足条件时
		charset[char] = true
		result = max(result, right-left+1)
	}
	return result
}
