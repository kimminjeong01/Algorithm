# 2023/04/25
# 점화식

n = int(input())
dp = [0] * (n+1)
dp[0] = 1
for i in range(1,n+1):
    for j in range(i):
        dp[i] += dp[i-1-j]*dp[j]
print(dp[n])