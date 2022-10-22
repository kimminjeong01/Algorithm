# 2022/10/18
# 서강근육맨

N = int(input())
health = list(map(int,input().split()))
health.sort()
result=[]
if N%2==0:
    for i in range(N):
        result.append(health[i]+health[N-i-1])
else:
    result.append(health[N-1])
    for i in range(N-1):
        result.append(health[i]+health[N-i-2])
print(max(result))