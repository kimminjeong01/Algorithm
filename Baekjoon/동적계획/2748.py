# 2022/10/04
# 피보나치 수 2

n= int(input())
dp= [-1]*(n+1)
dp[0]=0
dp[1]=1

# 하향식
def fibo(n):
    if dp[n]==-1:
        dp[n]=fibo(n-2)+fibo(n-1)
    
    return dp[n]


# # 상향식
# def fibo(n):
#     for i in range(2, n+1):
#         dp[i]= dp[i-1]+dp[i-2]
#     return dp[n]

print(fibo(n))