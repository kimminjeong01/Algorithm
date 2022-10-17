# 2022/10/17
# 에너지 드링크

cnt = int(input())
size = list(map(int,input().split()))

size.sort()
for i in range(cnt-1):
    size[i]/=2
print(sum(size))