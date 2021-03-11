import sys
'''
青蛙跳台阶问题变种
可以跳一级也可以跳两级，求有多少“种”跳法，本质还是斐波那契数列
'''

def countChoice(n, d_mine, m_tele):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        if i in d_mine:
            # 等价于 dp[i] = 0
            continue

        # choice from jump
        dp[i] = dp[i - 1] + dp[i - 2]

        # if any teleport to use
        for f, t in m_tele:
            if t == i:
                dp[i] += dp[f]


    return dp[n]


if __name__ == "__main__":
    '''
    n = 台阶长度
    d_mines = 地雷位置
    m_tele = 传送门（单向往上，如：5 7，从 5 传送到 7 层）
    '''
    n, d, m = sys.stdin.readline().strip().split()
    n = int(n)
    d_mine = sys.stdin.readline().strip().split()
    d_mine = list(map(int, d_mine))
    m_tele = sys.stdin.readline().strip().split()
    m_tele = list(map(int, m_tele))
    m_tele = [tuple(m_tele[i:i+2]) for i in range(0, len(m_tele), 2)]

    choice = countChoice(n, d_mine, m_tele)
    print(choice)
