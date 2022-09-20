# 2022/09/20
# 큐2

from collections import deque
import sys
num = int(sys.stdin.readline())

#deque 사용
queue = deque()
for i in range(num):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        if len(queue)==0:
            print(-1)
        else :
            print(queue.popleft())
    elif cmd[0] =="size":
        print(len(queue))
    elif cmd[0] =="empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif cmd[0] =="front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif cmd[0] =="back":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])




# 시간초과 -> 리스트로 구현
# queue=[]
# for i in range(num):
#     cmd = sys.stdin.readline().split()

#     if cmd[0] == "push":
#         queue.append(cmd[1])
#     elif cmd[0] == "pop":
#         if len(queue)==0:
#             print(-1)
#         else :
#             print(queue[0])
#             queue.remove(queue[0])
#     elif cmd[0] =="size":
#         print(len(queue))
#     elif cmd[0] =="empty":
#         if len(queue)==0:
#             print(1)
#         else:
#             print(0)
#     elif cmd[0] =="front":
#         if len(queue)==0:
#             print(-1)
#         else:
#             print(queue[0])
#     elif cmd[0] =="back":
#         if len(queue)==0:
#             print(-1)
#         else:
#             print(queue[len(queue)-1])
