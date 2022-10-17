# 2022/10/16
# 동전0

cnt, money = map(int,input().split())
coins=[0]*cnt
for i in range(cnt):
    coins[i]=int(input())
coins.sort(reverse=True)
result=0
for i in range(cnt):
    if money==0:
        break
    if money>=coins[i]:
        result+=money//coins[i]
        money%=coins[i]
print(result)