# 2023/04/19
# 토마토

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split())

graph = []
for i in range(N):
    cmd = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(cmd)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            queue.append((i,j))


def bfs():
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
            
bfs()

answer = 0
for g in graph:
    if 0 in g:
        print(-1)
        exit(0)
    answer = max(answer,max(g))
print(answer-1)



