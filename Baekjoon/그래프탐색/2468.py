# 2023/04/23
# 안전 영역

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = []
for i in range(N):
    cmd = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(cmd)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i,j,visited):
    queue = deque([(i,j)])
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if graph[nx][ny]!=0 and visited[nx][ny]==0:
                queue.append((nx,ny))
                visited[nx][ny] = 1


height = max(max(graph))

# 최소 1개
max_result = 1

for _ in range(height+1):
    for i in range(N):
        for j in range(N):
            if graph[i][j]>0:            
                graph[i][j]-=1 # 높이 1씩 줄임

    result = 0
    visited = [[0]*N for _ in range(N)] # 방문처리
    for i in range(N):
        for j in range(N):
            if graph[i][j]!=0 and visited[i][j]==0:
                bfs(i,j,visited)
                result += 1 # 구역 하나 추가

    if result>max_result:
        max_result = result
print(max_result)

        
