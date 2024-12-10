package leetcode

// numIslands TODO
// 200. 岛屿数量
func numIslands(grid [][]byte) int {
	length := len(grid)
	if length == 0 {
		return 0
	}

	count := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == '1' {
				dfs(grid, i, j)
				count++
			}
		}
	}
	return count
}

// dfs 岛屿类问题的通用解法、DFS 遍历框架
func dfs(grid [][]byte, i, j int) {
	// 判断 base case
	if !inArea(grid, i, j) {
		return
	}
	// 如果这个格子不是岛屿，直接返回
	if grid[i][j] != '1' {
		return
	}
	grid[i][j] = '2' // 将格子标记为「已遍历过」

	// 访问上、下、左、右四个相邻结点
	dfs(grid, i-1, j)
	dfs(grid, i, j-1)
	dfs(grid, i+1, j)
	dfs(grid, i, j+1)
}

func inArea(grid [][]byte, i, j int) bool {
	if len(grid) == 0 {
		return false
	}
	return i >= 0 && i < len(grid) &&
		j >= 0 && j < len(grid[0])
}
