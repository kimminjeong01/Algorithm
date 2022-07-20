# 2022/07/20
# 분해합

num = int(input())
for i in range(num+1):
    check=i
    if(check==num):
        print(0)
        break
    sum=i
    while(i>0):
        sum+=i%10
        i=i//10
    if(sum==num):
        print(check)
        break
    

# N = int(input())
# result = 0

# for i in range(1, N + 1):
#   tmp = i + sum(map(int,str(i)))

#   if tmp == N:
#     result = i
#     break

# print(result)