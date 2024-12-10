package leetcode

// minDistance TODO
// 72. 编辑距离
// DP
// 状态转移方程：D[i][j] = min(D[i][j-1]+1, D[i-1][j]+1, D[i-1][j-1]/D[i-1][j-1]+1)
//
//	add on A		add on B			modify on A
func minDistance(word1 string, word2 string) int {
	n, m := len(word1), len(word2)
	// 有一个字符串为空串
	if n*m == 0 {
		return n + m
	}
	D := make([][]int, n+1)
	for i := range D {
		D[i] = make([]int, m+1)
	}

	// init
	for i := range D {
		D[i][0] = i
	}
	for j := 0; j < m+1; j++ {
		D[0][j] = j
	}

	// DP
	for i := 1; i < n+1; i++ {
		for j := 1; j < m+1; j++ {
			left := D[i-1][j] + 1
			down := D[i][j-1] + 1
			leftDown := D[i-1][j-1]
			if word1[i-1] != word2[j-1] {
				leftDown += 1
			}
			D[i][j] = min(left, min(down, leftDown))
		}
	}
	return D[n][m]
}
