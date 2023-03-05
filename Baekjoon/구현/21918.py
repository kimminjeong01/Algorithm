#2023/03/05
# 전구

import sys
N, M = map(int, input().split())
lights = sys.stdin.readline().rstrip().split()
for i in range(M):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0]=='1':
        lights[int(cmd[1])-1]=cmd[2]
    elif cmd[0]=='2':
        for j in range(int(cmd[1])-1,int(cmd[2])):
            if lights[j]=='0':
                lights[j]='1'
            else:
                lights[j]='0'
    elif cmd[0]=='3':
        for j in range(int(cmd[1])-1,int(cmd[2])):
            lights[j]='0'
    elif cmd[0]=='4':
        for j in range(int(cmd[1])-1,int(cmd[2])):
            lights[j]='1'
for light in lights:
    print(light, end=' ')