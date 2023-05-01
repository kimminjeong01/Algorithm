# 2023/05/01
# 01 타일

n = int(input())
dp = [0] * (n+1)

for i in range(1,n+1):
    if i==1:
        dp[i] = 1
    elif i==2:
        dp[i] = 2
    else:
        # 메모리 초과되지 않게 반복문 안에서 나머지 연산자
        dp[i] = (dp[i-2] + dp[i-1])%15746
print(dp[n])