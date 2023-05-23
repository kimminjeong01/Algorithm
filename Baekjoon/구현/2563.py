# 2023/05/23
# 색종이

N = int(input())
paper = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = 1
result = 0
for p in paper:
    result += sum(p)
print(result)
