# 2023/04/18
# 숨바꼭질

from collections import deque

N, K = map(int,input().split())

dx = [1,-1,2]
graph = [-1]*100001

def bfs(start, end, graph):
    queue = deque([start])
    graph[start] = 0
    while queue:
        q = queue.popleft()
        for i in range(3):
            if i==2:
                nx = q * dx[i]
            else:
                nx = q + dx[i]
            if nx<0 or nx>100000:
                continue
            if graph[nx] == -1:
                queue.append(nx)
                graph[nx] = graph[q] + 1
            if nx == end:
                return graph[nx]

print(bfs(N,K,graph))
            


