# 2023/05/06
# 적록색약

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = [[0]*N for _ in range(N)]
graph2 = [[0]*N for _ in range(N)]

for i in range(N):
    cmd = sys.stdin.readline().rstrip()
    for j in range(N):
        graph[i][j] = cmd[j]
        graph2[i][j] = cmd[j]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs1(m,n,str):
    queue = deque([(m,n)])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if graph[nx][ny] == str:
                queue.append((nx,ny))
                graph[nx][ny] = 0

def bfs2(m,n,str):
    queue = deque([(m,n)])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if str=="R" or str=="G":
                if graph2[nx][ny] == "R" or graph2[nx][ny] == "G":
                    queue.append((nx,ny))
                    graph2[nx][ny] = 0
            else:
                if graph2[nx][ny] == str:
                    queue.append((nx,ny))
                    graph2[nx][ny] = 0

result1 = 0
result2 = 0
for i in range(N):
    for j in range(N):
        if graph[i][j]!=0:
            bfs1(i,j,graph[i][j])
            result1 += 1
        if graph2[i][j]!=0:
            bfs2(i,j,graph2[i][j])
            result2 += 1
print(result1, result2)