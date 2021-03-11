class UnionFind:                        #默写并查集模板
    def __init__(self, n):
        self.n = n
        self.part = n
        self.parent = [x for x in range(n)]
        self.size = [1 for _ in range(n)]

    def Find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        return self.Find(self.parent[x])

    def Union(self, x: int, y : int) -> bool:
        root_x = self.Find(x)
        root_y = self.Find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] =  root_y
        self.size[root_y] += self.size[root_x]
        self.part -= 1
        return True

    def inthesamepart(self, x: int, y : int) -> bool:
        return self.Find(x) == self.Find(y)

    def getpartsize(self, x: int) -> int:
        root_x = self.Find(x)
        return self.size[root_x]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        UF = UnionFind(R * C)
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:                 #初始化并查集  把陆地都连接在一起
                    for dr,dc in ((1, 0), (0, 1)):
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                            UF.Union(r * C + c,   nr * C + nc)
        res = max(UF.size)                          #当前最大的区域
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:                 #按照题意  把一块海洋，变成陆地
                    tmp = 1                         #当前这块就 + 1
                    root_set = set()
                    for dr,dc in ((-1,0), (0,1), (1,0), (0,-1)):    #4个方向  最多有可能连接4块区域
                        nr,  nc = r + dr,  c + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:   #在矩阵内 且是陆地
                            part_root = UF.Find(nr * C + nc)
                            if part_root not in root_set:                       #且还没统计过
                                tmp += UF.size[part_root]
                                root_set.add(part_root)
                    res = max(res, tmp)
        return res
