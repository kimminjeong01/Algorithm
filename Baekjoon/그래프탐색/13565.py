# 2023/04/14
# 침투

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split())
graph = [[0]*N for i in range(M)]
for i in range(M):
    cmd = sys.stdin.readline().rstrip()
    for j in range(N):
        graph[i][j] = int(cmd[j])


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(i, j, graph):
    queue = deque([(i,j)])
    graph[i][j]=1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx == M-1 :
                return 1
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if graph[nx][ny]==0:
                queue.append((nx,ny))
                graph[nx][ny]=1
    return 0

result = "NO"
for i in range(N):
    if graph[0][i]==0:
        if bfs(0,i,graph) == 1:
            result = "YES"

print(result)

        
