# 2023/04/26
# 돌 게임 2

N = int(input())
result = [-1]*1001
result[1] = 1
result[2] = 0
result[3] = 1

# for i in range(4,N+1):
#     if result[i-1]==1:
#         result[i]=0
#     else:
#         result[i]=1

for i in range(4,N+1):
    if result[i-1]==1 or result[i-3]==1:
        result[i]=0
    else:
        result[i]=1

if result[N]==1:
    print("CY")
else:
    print("SK")