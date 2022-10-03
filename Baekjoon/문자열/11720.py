#2022/10/03
# 숫자의 합

N = int(input())
numList = list(map(int,input()))

sum=0
for i in numList:
    sum+=i
print(sum)