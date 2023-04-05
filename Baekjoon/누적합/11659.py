# 2023/04/05
# 구간 합 구하기 4

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

nums = list(map(int, sys.stdin.readline().rstrip().split()))
sums = [0]*(n+1)

for i in range(n):
    sums[i+1] = sums[i] + nums[i]

for i in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    print(sums[end]-sums[start-1])