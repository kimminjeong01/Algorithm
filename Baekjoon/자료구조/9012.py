# 2022/09/19
# 괄호    

num = int(input())
 
for i in range(num):
    stack = []
    str = input()

    for char in str:
        if char=='(':
            stack.append(char)
        elif len(stack)!=0:
            if char==')' and stack[len(stack)-1]=='(':
                stack.pop()
        elif char==')' and len(stack)==0:
            stack.append(char)
        
    if len(stack)==0:
        print("YES")
    else :
        print("NO")

    