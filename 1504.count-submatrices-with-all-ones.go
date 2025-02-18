package leetcode

func numSubmat(mat [][]int) int {
	n, m := len(mat), len(mat[0])
	rows := make([][]int, n)
	for i := range rows {
		rows[i] = make([]int, m)
	}

	// 生成 rows 的数据，求和从当前位置向左的连续 1 的个数
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if mat[i][j] == 1 {
				if j == 0 {
					rows[i][j] = 1
				} else {
					rows[i][j] = rows[i][j-1] + 1
				}
			}
		}
	}

	var ans int
	// 从每个位置开始，逆序遍历，找到最小的行数，然后计算所有可能的矩形个数
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if mat[i][j] != 1 {
				continue
			}
			col := rows[i][j]
			for k := i; k >= 0; k-- {
				col = min(col, rows[k][j])
				ans += col
			}
		}
	}

	return ans
}
