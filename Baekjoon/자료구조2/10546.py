# 2022/10/14
# 배부른 마라토너

import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = []
for _ in range(n+n-1):
    a.append(input().rstrip())

dic = {}

for i in range(n):
    dic[a[i]] = dic.get(a[i],0)+1

for i in range(n,len(a)):
    dic[a[i]] = dic.get(a[i],0)-1

for k,v in dic.items():
    if v>0:
        print(k)


# # 리스트로 풀면 시간초과 발생
# N = int(input())
# runners=[]
# for i in range(N):
#     name = input()
#     runners.append(name)

# for j in range(N-1):
#     name = input()
#     if name in runners:
#         runners.remove(name)

# print(runners[0])