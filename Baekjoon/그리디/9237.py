# 2023/04/13
# 이장님 초대

import sys

num = int(sys.stdin.readline().rstrip())
cmd = list(map(int,sys.stdin.readline().rstrip().split()))
cmd.sort(reverse=True)

for i in range(num):
    cmd[i] = cmd[i]+i+1

print(max(cmd)+1)


