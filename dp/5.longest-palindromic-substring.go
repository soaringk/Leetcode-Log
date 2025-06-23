package leetcode

// longestPalindrome TODO
// 5. 最长回文子串
func longestPalindrome(s string) string {
	n := len(s)
	if n <= 1 {
		return s
	}
	D := make([][]bool, n)
	for i := range D {
		D[i] = make([]bool, n)
	}
	// init: 长度为 1 的子串都是回文
	for i := 0; i < n; i++ {
		D[i][i] = true
	}
	maxLength := 1
	start := 0
	// 状态转移方程，D[i][j] = (D[i+1][j-1] || 少于等于两个字符) && s[i] == s[j]
	for L := 2; L <= n; L++ { // 从长度较短的字符串向长度较长的字符串进行转移的，因此一定要注意动态规划的循环顺序。
		for i := 0; i < n; i++ {
			j := i + L - 1 // j - i + 1 = L
			if j >= n {
				break
			}

			if s[i] == s[j] && (j-i <= 2 || D[i+1][j-1]) {
				D[i][j] = true
				if maxLength < L {
					maxLength = L
					start = i
				}
			}
		}
	}
	return s[start : start+maxLength]
}
