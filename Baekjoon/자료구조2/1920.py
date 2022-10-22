# 2022/10/22
# 수 찾기
# 이분탐색으로도 풀어보기

import sys

N = int(input())
# 집합으로 설정
nums = set(map(int,sys.stdin.readline().split()))
M = int(input())
checkNums = list(map(int, sys.stdin.readline().split()))

for num in checkNums:
    if num in nums:
        print(1)
    else:
        print(0)