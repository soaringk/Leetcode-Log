n = 5
m = 3

def lastRemaining(n, m):
    dp = [0 for _ in range(n + 1)]

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + m) % i

    return dp[n]

res = lastRemaining(n, m)
print(res)
