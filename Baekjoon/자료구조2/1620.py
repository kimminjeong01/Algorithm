# 2022/10/27
# 나는야 포켓몬 마스터 이다솜

# import sys
# cnt, rst = map(int, sys.stdin.readline().split())
# pocketmons = {}
# for i in range(cnt):
#     name=input()
#     pocketmons[i+1]=name
#     pocketmons[name]=i+1

# for j in range(rst):
#     str = input()
#     if str.isdigit():
#         print(pocketmons[int(str)])
#     else:
#         print(pocketmons[str])

# pocketmons = []
# for i in range(cnt):
#     pocketmons.append(input())
# for j in range(rst):
#     str = input()
#     if str.isdigit():
#         print(pocketmons[int(str)])
#     else:
#         print(pocketmons.index(str)+1)

import sys
input = sys.stdin.readline
cnt, rst = map(int, input().split())

pocketmons = {}
for i in range(1, cnt+1):
    str = input().rstrip()
    pocketmons[i]=str
    pocketmons[str]=i

for j in range(rst):
    quest = input().rstrip()
    if quest.isdigit():
        print(pocketmons[int(quest)])
    else:
        print(pocketmons[quest])