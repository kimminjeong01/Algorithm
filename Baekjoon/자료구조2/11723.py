# 2022/10/25
# 집합

import sys

results=set()
N = int(input())
for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0]=="add":
        if cmd[1] not in results:
            results.add(cmd[1])
    elif cmd[0]=="remove":
        if cmd[1] in results:
            results.remove(cmd[1])
    elif cmd[0]=="check":
        if cmd[1] in results:
            print(1)
        else:
            print(0)
    elif cmd[0]=="toggle":
        if cmd[1] in results:
            results.remove(cmd[1])
        else:
            results.add(cmd[1])
    elif cmd[0]=="all":
        results.clear()
        results={'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
    elif cmd[0]=="empty":
        results.clear()
    