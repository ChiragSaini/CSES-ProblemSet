MOD = int(10e9 + 7)
n = int(input())
dp = [0]*int(n+1)
dp[0] = 1
for i in range(1, n+1):
    for x in range(1, 7):
        if x > i:
            break
        dp[i] = (dp[i] + dp[i-x]) % MOD
print(dp[n])
