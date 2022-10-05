# 2022/10/05
# 돌게임

N = int(input())
result = [-1]*10000

result[1]=1 # sk
result[2]=0 # cy
result[3]=1 # sk

for i in range(4,N+1):
    if result[i-1]==1 or result[i-3]==1:
        result[i]=0
    else:
        result[i]=1

if result[N]==1:
    print("SK")
else:
    print("CY")        

# if N%2==0:
#     print('CY')
# else:
#     print('SK')


