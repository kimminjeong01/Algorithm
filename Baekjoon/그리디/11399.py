# 2022/10/15
# ATM

num = int(input())
atmLine = list(map(int,input().split()))

atmLine.sort()
result=0
for i in range(num):
    for j in range(i+1):
        result+=atmLine[j]
print(result)