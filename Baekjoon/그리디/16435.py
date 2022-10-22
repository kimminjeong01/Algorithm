# 2022/10/18
# 스네이크 버드

cnt, tall = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()

for i in range(cnt):
    if tall>=heights[i]:
        tall+=1
print(tall)