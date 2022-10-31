# 2022/10/31
# 빠른 A+B

import sys
num = int(input())

for i in range(num):
    cmd = sys.stdin.readline().rsplit()
    print(int(cmd[0])+int(cmd[1]))