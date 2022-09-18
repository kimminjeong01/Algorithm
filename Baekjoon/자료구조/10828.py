# 2022/09/19
# 스택

import sys
num = int(sys.stdin.readline())

stack=[]
for i in range(num):
    cmd = sys.stdin.readline().split()

    if cmd[0]=="push":
        stack.append(cmd[1])
    elif cmd[0]=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd[0]=="size":
        print(len(stack))
    elif cmd[0]=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]=="top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[len(stack)-1])

# class Stack():
#     def __init__(self):
#         self.stack=[]

#     def push(self,x):
#         self.stack.append(x)

#     def pop(self):
#         if self.size()==0:
#             return -1
#         return self.stack.pop()

#     def size(self):
#         if(len(self.stack)==0):
#             return 0
#         return len(self.stack)

#     def empty(self):
#         if self.size()==0:
#             return 1
#         return 0

#     def top(self):
#         if self.size()==-1:
#             return -1
#         return self.stack[self.size()-1]

# num = int(input())
# str_list=[]
# for i in range(num):
#     str_list.append(input())

# stack = Stack()
# for i in range(num):
#     if "push" in str_list[i]:
#         x,y=str_list[i].split()
#         stack.push(y)
#     elif str_list[i]=="pop":
#         print(stack.pop())
#     elif str_list[i]=="size":
#         print(stack.size())
#     elif str_list[i]=="empty":
#         print(stack.empty())
#     elif str_list[i]=="top":
#         print(stack.top())




