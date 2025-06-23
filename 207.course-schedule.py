#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
from collections import defaultdict, deque
from typing import List

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # bfs 广度优先遍历，遍历每个入度为 0 的节点并将其加入遍历结果队列，同时将有边的节点的入度递减
        edges, indeg, visited = defaultdict(list), [0] * numCourses, 0
        for (cour, pre) in prerequisites:
            edges[pre].append(cour)
            indeg[cour] += 1
        
        q = deque([u for u in range(numCourses) if indeg[u] == 0])
        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses
# @lc code=end

