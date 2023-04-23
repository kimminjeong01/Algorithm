# 2023/04/23
# 패션왕 신해빈

import sys
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    case = dict()
    for i in range(n):
        cmd = sys.stdin.readline().rstrip().split()
        if cmd[1] in case:
            case[cmd[1]] += 1
        else: 
            case[cmd[1]] = 1
    result = 1
    for c in case:
        result *= (case[c]+1)
    print(result-1)
