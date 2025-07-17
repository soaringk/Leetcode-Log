from typing import List
from collections import defaultdict

class Vertex:
    def __init__(self, value, edges=None):
        self.value = value
        self.edges = edges if edges is not None else []

# 检查有向图是否有环
# 存两个状态， 1 表示访问过但未完成， 2 表示访问过且已完成
def checkGraphLoop(vertexes: List[Vertex], edges: List[tuple]) -> bool:
    visited = defaultdict(int)

    # 构建邻接表
    for u, v in edges:
        vertexes[u - 1].edges.append(vertexes[v - 1])

    def visit(vertex):
        visited[vertex.value] = 1  # 标记为访问中
        for neighbor in vertex.edges:
            if visited[neighbor.value] == 1 or (visited[neighbor.value] == 0 and visit(neighbor)):
                return True

        visited[vertex.value] = 2
        return False

    for v in vertexes:
        if visited[v.value] == 2:
            continue
        if visit(v):
            return True

    return False

# data = [
#     # Vertex(1, [Vertex(1)]),
#     Vertex(1, [Vertex(2), Vertex(3)]),
#     Vertex(2, [Vertex(4)]),
#     Vertex(3, [Vertex(4)]),
#     Vertex(4, [Vertex(1)]),
# ]
vertexes = [Vertex(1), Vertex(2), Vertex(3), Vertex(4)]
edges = [
    (1, 2), (1, 3), (2, 4),
    (3, 4), (4, 1)
]
print(checkGraphLoop(vertexes, edges))
