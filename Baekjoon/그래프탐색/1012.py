# 2023/04/08
# 유기농 배추

import sys
from collections import deque

# 테스트 케이스 개수
T = int(sys.stdin.readline().rstrip())

# 상하좌우 이동
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 그래프 탐색
def bfs(graph, a, b):
    queue = deque([(a,b)])
    # 1인 칸은 탐색했다는 표시로 0으로 변경
    graph[a][b]=0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))


for _ in range(T):
    result = 0
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0]*M for _ in range(N)]
    for _ in range(K):
        cmd = list(map(int,sys.stdin.readline().rstrip().split()))
        graph[cmd[1]][cmd[0]] = 1

    # 그래프가 1인 곳부터 탐색 시작
    for a in range(N):
        for b in range(M):
            if graph[a][b]==1:
                bfs(graph, a, b)
                result +=1
    print(result)