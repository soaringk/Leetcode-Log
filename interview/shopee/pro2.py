import sys
'''
走棋盘，选定第一行某一处作为起点，遍历棋盘中的所有黑格子，求最小步数
[
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 1, 0]
]
好像答案是 8
路线是
    [0, (0),  0,   0 ],
    [0, (1), (0), (0)],
    [0,  0,   0,  (1)],
    [0, (1), (1), (0)]
'''

def findShortestPath(matrix, m, n) -> int:
    visited = [[False] * m for _ in range(n)]
    step = 0

    def backtrack(paths, choices):
        if True:
            res

    # 选起点
    for row in range(len(matrix)):
        if max(matrix[row]) != 0:
            start = [(row, i) for i, v in enumerate(matrix[row]) if v]
            break

    for row, col in start:
        step += row
        backtrack()

if __name__ == "__main__":
    t = sys.stdin.readline().strip()
    for i in range(int(t)):
        n, m = sys.stdin.readline().strip().split()
        n, m = int(n), int(m)
        maxtrix = [[0] * m for _ in range(n)]
        for i in range(n):
            line = sys.stdin.readline().strip().split()
            if line[0] != '0':
                for k in range(int(line[0])):
                    col = int(line[k + 1])
                    maxtrix[i][col - 1] = 1

        res = findShortestPath(maxtrix, m, n)
        print(res)
