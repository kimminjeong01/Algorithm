# 2023/04/24
# 파도반 수열

dp = [1] * (101)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(6,N+1):
        if dp[i]==1:
            dp[i] = dp[i-1] + dp[i-5]
    print(dp[N])
