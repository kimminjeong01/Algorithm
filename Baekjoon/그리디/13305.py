# 2022/10/17
# 주유소

cnt = int(input())
distance = list(map(int,input().split()))
oil_cost=list(map(int,input().split()))
now = oil_cost[0]

result=0

for i in range(len(oil_cost)-1):
    if now>oil_cost[i]:
        now = oil_cost[i]
    result+=now * distance[i]

print(result)
    


