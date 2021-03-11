#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        def dfs(grid, row, col):
            grid[row][col] = 0
            n, m = len(grid), len(grid[0])
            for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] == "1":
                    dfs(grid, x, y)

        num_islands = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == '1':
                    num_islands += 1
                    dfs(grid, row, col)

        return num_islands


# @lc code=end
