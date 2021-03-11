import sys
'''
走棋盘，选定第一行某一处作为起点，遍历棋盘中的所有黑格子，求最小步数，行走时可选方向：左、右、下
[
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 1, 0]
]
note: 1 表示该处为黑格子
好像答案是 8
路线是
[
    [0, {0},  0,   0 ],
    [0, {1}, {0}, {0}],
    [0,  0,   0,  {1}],
    [0, {1}, {1}, {0}]
]

思路：每一层都应该走到最左边的1或者最右边的1这样距离是最小的，
所以用一个dp[m][n]或者dp[n]循环m次计算到当前这一层的最左边的1和最右边的1的最短距离，
到最后一层取较小的那个值就可以了
'''

def findShortestPath(matrix, m, n) -> int:
    '''
    可能还要加一个计步器？目前没有是否遍历全部节点的判断
    '''
    # 选起点
    for row in range(len(matrix)):
        if max(matrix[row]) != 0:
            start = [i for i, v in enumerate(matrix[row]) if v]
            break
    start = [min(start), max(start)]
    # 只留一个最靠近边界的
    if start[1] + start[0] > m - 1:    # 计算中点
        start = [start[1]]
    elif start[1] + start[0] < m - 1:
        start = [start[0]]

    min_path = float('inf')
    # 对于一个起点
    for col in start:
        dp = [[float('inf')] * m for _ in range(n + 1)]

        # base case
        dp[0][col] = 0
        dp[1][col] = 1
        dir_to_right = True # 还是改成while吧，待续
        for r in range(1, n + 1):
            # 寻找最左和最右的 1，判断要去哪里
            ends = [i for i, v in enumerate(matrix[r - 1]) if v == 1]
            if not ends:
                # 这一层没有 1，跳过
                continue
            if len(ends) > 1:
                ends = [min(ends), max(ends)]

            for end in ends:
                dp[r][end] = min(
                    dp[r][end],
                    dp[r - 1][m - 1] + 1 + (m - 1 - end),
                    dp[r - 1][0] + 1 + end
                )
                # 如果上面是黑色才可以直接往下走
                if matrix[r - 1][end] == 1:
                    dp[r][end] = min(dp[r][end], dp[r - 1][end] + 1)
            for c in range(m):

                # 计算到最左或最右的最短距离
                for end in ends:
                    dp[r][c] = min(
                        dp[r][c],
                        dp[r][end] + abs(end - c)
                    )

        choices = [dp[r][i + 1] for i, v in enumerate(matrix[r - 1]) if v == 1]
        min_path = min(min_path, max(choices))

    return min_path


# if __name__ == "__main__":
#     t = sys.stdin.readline().strip()
#     for i in range(int(t)):
#         n, m = sys.stdin.readline().strip().split()
#         n, m = int(n), int(m)
#         matrix = [[0] * m for _ in range(n)]
#         for i in range(n):
#             line = sys.stdin.readline().strip().split()
#             if line[0] != '0':
#                 for k in range(int(line[0])):
#                     col = int(line[k + 1])
#                     matrix[i][col - 1] = 1

#         res = findShortestPath(matrix, m, n)
#         print(res)

matrix = [[1, 0, 0, 1], [0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 1, 0]]
res = findShortestPath(matrix, 4, 4)
print(res)
