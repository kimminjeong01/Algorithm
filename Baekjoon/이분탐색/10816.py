# 2023/04/16
# 숫자 카드 2

import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

nums_count = dict()
for num in nums:
    if num in nums_count:
        nums_count[num] += 1
    else:
        nums_count[num] = 1

M = int(sys.stdin.readline().rstrip())
check_nums = list(map(int, sys.stdin.readline().rstrip().split()))
for c in check_nums:
    if c in nums_count:
        print(nums_count[c], end=' ')
    else:
        print(0, end=' ')

