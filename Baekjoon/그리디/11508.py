# 2022/10/16
# 2+1 세일

num = int(input())
cost=[0]*num

for i in range(num):
    cost[i]=int(input())

cost.sort(reverse=True)
money=sum(cost)
for i in range(2,num,3):
    money-=cost[i]

print(money)

