# 2022/09/19
# 괄호    

num = int(input())
for i in range(num):
    str= input()
    sum = 0
    for char in str:
        if char =="(":
            sum +=1
        elif char ==")":
            sum -=1
        
        if sum<0:
            print("NO")
            break
        
    if sum == 0:
        print("YES")
    elif sum >0:
        print("NO")

# num = int(input())
 
# for i in range(num):
#     stack = []
#     str = input()

#     for char in str:
#         if char=='(':
#             stack.append(char)
#         elif len(stack)!=0:
#             if char==')' and stack[len(stack)-1]=='(':
#                 stack.pop()
#         elif char==')' and len(stack)==0:
#             stack.append(char)
        
#     if len(stack)==0:
#         print("YES")
#     else :
#         print("NO")

    