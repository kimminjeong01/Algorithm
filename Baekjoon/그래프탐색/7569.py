# 2023/05/15
# 토마토

import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().rstrip().split())

graph = [[[0]*M for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        cmd = list(map(int, sys.stdin.readline().rstrip().split()))
        graph[i][j] = cmd

dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k]==1:
                queue.append((j,k,i))


def bfs():
    while queue :
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx<0 or ny<0 or nz<0 or nx>=N or ny>=M or nz>=H:
                continue
            if graph[nz][nx][ny]==0:
                graph[nz][nx][ny]=graph[z][x][y]+1
                queue.append((nx,ny,nz))
            
bfs()

answer = 0
for g1 in graph:
    for g2 in g1:
        if 0 in g2:
            print(-1)
            exit(0)
        answer = max(answer,max(g2))
print(answer-1)
