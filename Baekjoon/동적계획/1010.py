# 2022/10/11
# 다리놓기

dp = [[1] * 31 for _ in range(31)]
for i in range(31):
    dp[1][i] = i
for i in range(2, 31):
    for j in range(i + 1, 31):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])


# import math
# T = int(input())
# for _ in range(T):
#     n, m = map(int, input().split())
#     case = math.factorial(m)//(math.factorial(n)*math.factorial(m-n))
#     print(case)

# #시간초과
# from itertools import combinations

# T = int(input())
# for i in range(T):
#     x,y = map(int,input().split())
#     case = len(list(combinations(range(y),x)))
#     print(case)