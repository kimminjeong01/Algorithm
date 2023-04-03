# 2023/04/03
# 스택 수열

# n = int(input())

# nums = []
# for i in range(n):
#     nums.append(int(input()))

# stack1 = []
# stack2= [i for i in range(1,n+1)]
# result = []

# while (True):
#     if len(nums)==0:
#         for r in result:
#             print(r)
#         break

#     if len(stack2)!=0:
#         stack1.append(stack2.pop(0))
#         result.append("+")

#     while(stack1[-1]==nums[0]):
#         stack1.pop(-1)
#         nums.pop(0)
#         result.append("-")

#         if len(stack1)==0:
#             break
    
#     if len(stack2)==0 and len(nums)!=0:
#         print("NO")
#         break


count = 1
temp = True
stack = []
result = []

N = int(input())
for i in range(N):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        temp = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력 
if temp == False:
    print("NO")
else:
    for i in result:
        print(i)
    

    


