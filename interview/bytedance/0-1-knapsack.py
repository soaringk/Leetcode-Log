'''
0-1背包问题
有 n 个文件，硬盘容量是 S，想办法让硬盘塞完文件后剩余容量最少
'''

files = [1, 2, 3, 5, 7]
S = 11

def getMinimumRemainder(files, S):
    n = len(files)
    dp = [[float('inf')] * (n + 1) for _ in range(S + 1)]

res = getMinimumRemainder(files, S)
