# 2023/04/09
# N번째 큰 수

import sys
T = int(input())
for _ in range(T):
    cmd = list(map(int, sys.stdin.readline().rstrip().split()))
    cmd.sort(reverse=True)
    print(cmd[2])