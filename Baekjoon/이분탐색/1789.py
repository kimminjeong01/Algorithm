# 2023/01/24
# 수들의 합

N = int(input())
result = 1
sum = 1
while(True):
    result+=1
    sum+=result
    if sum>N:
        print(result-1)
        break