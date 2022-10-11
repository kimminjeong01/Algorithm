# 2022/10/11
# 덱

from collections import deque
import sys

deq = deque()
num = int(input())
for i in range(num):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push_front":
        deq.appendleft(cmd[1])
    elif cmd[0]=="push_back":
        deq.append(cmd[1])
    elif cmd[0]=="pop_front":
        if len(deq)==0:
            print(-1)
        else:
            print(deq.popleft())
    elif cmd[0]=="pop_back":
        if len(deq)==0:
            print(-1)
        else:
            print(deq.pop())
    elif cmd[0]=="size":
        print(len(deq))
    elif cmd[0]=="empty":
        if len(deq)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]=="front":
        if len(deq)==0:
            print(-1)
        else:
            print(deq[0])
    elif cmd[0]=="back":
        if len(deq)==0:
            print(-1)
        else:
            print(deq[-1])