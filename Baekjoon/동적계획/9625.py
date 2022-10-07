# 2022/10/07
# BABBA

num= int(input())
dp=[0]*(num+1)
dp[1]=1

def countAB(k):
    for i in range(2, k+1):
        dp[i]= dp[i-1]+dp[i-2]

countAB(num)

# 결과가 피보나치 수열을 따름
print(dp[num-1], dp[num])