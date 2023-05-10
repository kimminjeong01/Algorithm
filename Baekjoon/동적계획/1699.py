# 2023/05/10
# 제곱수의 합

N = int(input())
dp = [0]*(100001)

dp[1]=1
dp[2]=2
dp[3]=3

for i in range(4,N+1):
    dp[i] = i
    for j in range(1,i):
            if j*j>i:
                break
            if dp[i]>dp[i-j*j] + 1:
                dp[i] = dp[i-j*j]+1
print(dp[N])