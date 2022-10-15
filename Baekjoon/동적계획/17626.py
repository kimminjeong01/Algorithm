# 2022/10/13
# Four Squares

import math

num = int(input())
result_list=[0]*(num+1)
result_list[1]=1

sqr= math.sqrt(num+1)
if sqr==int(sqr):
    print(1)
else:
    for i in range(2,num+1):
        if i == int(math.sqrt(i))**2:
            result_list[i]=1
        else:
            l=[]
            for j in range(1,math.floor(math.sqrt(i))+1):
                l.append(result_list[i-(j**2)]+1)
            result_list[i]=min(l)
    print(result_list[num])




    
# import math
# num = int(input())

# result_list=[100]*(num+1)
# result_list[0]=1
# result_list[1]=2
# for i in range(num):
#     sqr= math.sqrt(i+1)
#     if sqr==int(sqr):
#         result_list[i]=1
#     else:
#         for j in range(i):
#             cur = result_list[i]
#             new = result_list[i-j-1]+result_list[j]
#             if cur>new:
#                 result_list[i]=new

# print(result_list[num-1])