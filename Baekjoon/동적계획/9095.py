# 2023/04/29
# 1,2,3 더하기

T = int(input())
for _ in range(T):
    n= int(input())
    dp = [0]*11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n+1):
        if dp[i] == 0:
            # n-3에 3을 더함, n-2에 2를 더함, n-1에 1을 더함
            # 따라서 인덱스가 n-3, n-2, n-1일 때를 더하면 됨
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])