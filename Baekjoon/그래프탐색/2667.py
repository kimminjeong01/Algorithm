# 2023/04/11
# 단지번호 붙이기

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = [[0]*N for _ in range(N)]

for i in range(N):
    cmd = sys.stdin.readline().rstrip()
    for j in range(N):
        graph[i][j] = cmd[j]

result = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a, b, graph):
    queue = deque([(a,b)])
    graph[a][b] = '0'
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if graph[nx][ny]=='1':
                cnt += 1
                graph[nx][ny]='0'
                queue.append((nx,ny))
    return cnt


for i in range(N):
    for j in range(N):
        if graph[i][j]=='1':
            result.append(bfs(i,j,graph))

result.sort()
print(len(result))
for r in result:
    print(r)
