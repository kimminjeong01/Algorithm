# 2022/10/09
# 알바생 강호

num = int(input())

tip = []
for i in range(num):
    tip.append(int(input()))

tip.sort(reverse=True)
total=0
for i in range(num):
    add = tip[i]-i
    if add>0:
        total+=add
print(total)