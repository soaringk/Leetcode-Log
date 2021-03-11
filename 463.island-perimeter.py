#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])

        def dfs(grid, r, c):
            if not (0 <= r < n and 0 <= c < m):
                return 1
            if grid[r][c] == 0:
                return 1
            if grid[r][c] == 2:
                return 0
            grid[r][c] = 2
            return dfs(grid, r - 1, c) \
                    + dfs(grid, r + 1, c) \
                    + dfs(grid, r, c - 1) \
                    + dfs(grid, r, c + 1)

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    perimeter = dfs(grid, r, c)
                    res = max(res, perimeter)
                    # return perimeter

        return res

# @lc code=end
