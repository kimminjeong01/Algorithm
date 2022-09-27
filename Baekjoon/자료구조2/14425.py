# 2022/ 09/ 27
# 문자열 집합

n, m = map(int, input().split())

str_list=set()
for i in range(n):
    str_list.add(input())

cnt = 0
for i in range(m):
    str = input()
    if str in str_list:
        cnt+=1

print(cnt)

# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# s = set([input() for _ in range(N)])
# cnt = 0
# for _ in range(M):
#     t = input()
#     if t in s:
#         cnt += 1
# print(cnt)
