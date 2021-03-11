#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#
from typing import List
# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        '''
        第一遍 DFS 遍历陆地格子，计算每个岛屿的面积并标记岛屿；
        第二遍 DFS 遍历海洋格子，观察每个海洋格子相邻的陆地格子。
        '''
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])

        def build_island(grid, r, c, flag):
            if not (0 <= r < n and 0 <= c < m and grid[r][c] == 1):
                return 0
            grid[r][c] = flag
            return 1 \
                    + build_island(grid, r - 1, c, flag) \
                    + build_island(grid, r + 1, c, flag) \
                    + build_island(grid, r, c - 1, flag) \
                    + build_island(grid, r, c + 1, flag)

        island_size = {}
        island_size[0] = 0
        flag = 2
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = build_island(grid, r, c, flag)
                    island_size[flag] = area
                    flag += 1

        if not island_size.values():
            return 1

        def replace_sea(grid, r, c):
            if not (0 <= r < n and 0 <= c < m):
                return 0

            neighbor = set()
            if 0 < r:
                up = grid[r - 1][c]
                neighbor.add(up)
            if r < n - 1:
                down = grid[r + 1][c]
                neighbor.add(down)
            if 0 < c:
                left = grid[r][c - 1]
                neighbor.add(left)
            if c < m - 1:
                right = grid[r][c + 1]
                neighbor.add(right)

            size = list(map(island_size.get, neighbor))
            return 1 + sum(size)

        res = max(island_size.values())
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    new_area = replace_sea(grid, r, c)
                    res = max(res, new_area)

        return res

# @lc code=end
s = Solution()
s.largestIsland([[1, 0, 1], [0, 0, 0], [0, 1, 1]])
