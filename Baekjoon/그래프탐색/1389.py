# 2023/03/29
# 케빈 베이컨의 6단계 법칙

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[]*(n+1) for _ in range(n+1)]

for i in range(m):
    cmd = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[cmd[0]].append(cmd[1])
    graph[cmd[1]].append(cmd[0])

result = [9999]*(n+1)
def bfs(start):
    queue = deque([start])
    visited = [-1] *(n+1)
    visited[start] = 0

    while queue :
        v = queue.popleft()

        for i in graph[v]:
            if visited[i]==-1:
                queue.append(i)
                visited[i]=visited[v]+1
    result[start] = sum(visited) + 1

for i in range(1, n+1):
    bfs(i)
    
print(result.index(min(result)))