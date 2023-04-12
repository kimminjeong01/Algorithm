# 2023/04/12
# 섬의 개수

import sys
from collections import deque

dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

def bfs(i, j, graph):
    queue = deque([(i,j)])
    graph[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=h or ny>=w:
                continue
            if graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny]=0  

while(True):
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if (w==0 and h ==0):
        break
    graph=[[0]*w for _ in range(h)]
    for i in range(h):
        cmd = sys.stdin.readline().rstrip().split()
        for j in range(w):
            graph[i][j]=int(cmd[j])
    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                bfs(i, j, graph)
                result += 1
    print(result)



