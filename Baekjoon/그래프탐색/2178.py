# 2023/04/09
# 미로 탐색

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = [[0]*M for _ in range(N)]

for i in range(N):
    cmd = sys.stdin.readline().rstrip()
    for j in range(M):
        graph[i][j]=int(cmd[j])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph):
    queue = deque([(0,0)])
    graph[0][0]=1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
    print(graph[N-1][M-1])

bfs(graph)