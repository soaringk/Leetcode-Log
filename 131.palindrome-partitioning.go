package leetcode

func partition(s string) [][]string {
	var isPalindrome = func(s string, left, right int) bool {
		for left < right {
			if s[left] != s[right] {
				return false
			}
			left++
			right--
		}
		return true
	}

	ans := [][]string{}
	n := len(s)
	path := []string{}

	var dfs func(int, int)
	// start 表示当前回溯的回文子串的起始位置
	dfs = func(end, start int) {
		if end == n {
			ans = append(ans, append([]string(nil), path...)) // copy
			return
		}

		// 不选 i 和 i+1之间的逗号（i=n-1时一定要选）
		if end < n-1 {
			dfs(end+1, start)
		}

		// 选 i 和 i+1之间的逗号
		if isPalindrome(s, start, end) {
			path = append(path, s[start:end+1])
			dfs(end+1, end+1)
			path = path[:len(path)-1]
		}
	}

	dfs(0, 0)
	return ans
}
