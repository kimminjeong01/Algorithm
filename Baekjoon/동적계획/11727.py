# 2023/04/30
# 2*n 타일링 2

n = int(input())
dp = [0]*1001
dp[1]=1
dp[2]=3

for i in range(3, n+1):
    if dp[i] == 0:
        dp[i] = 2*dp[i-2] + dp[i-1]

result = dp[n]%10007
print(result)