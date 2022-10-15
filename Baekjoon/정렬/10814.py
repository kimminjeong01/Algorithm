# 2022/10/14
# 나이순 정렬

N = int(input())

arr = []
for i in range(N):
    str = input()
    arr.append(str)
arr.sort()
for str in arr:
    print(str)