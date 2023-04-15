# 2023/04/15
# 나이트의 이동

import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())

dx = [1,1,-1,-1,2,2,-2,-2]
dy = [2,-2,2,-2,1,-1,1,-1]

def bfs(i, j, di, dj, graph):
    queue = deque([(i,j)])
    graph[i][j]=0
    
    if i==di and j==dj:
        return 0
    
    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx<0 or ny<0 or nx>=I or ny>=I:
                continue
            if graph[nx][ny]==0:
                queue.append((nx,ny))
                graph[nx][ny]= graph[x][y] + 1
            if nx == di and ny == dj:
                return graph[di][dj]



for _ in range(N):
    I = int(sys.stdin.readline().rstrip())
    graph = [[0]*I for _ in range(I)]
    i, j = map(int, sys.stdin.readline().rstrip().split())
    di, dj = map(int, sys.stdin.readline().rstrip().split())
    print(bfs(i,j,di,dj,graph))
