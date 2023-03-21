# 2023/03/21
# 연결 요소의 개수

import sys
from collections import deque

n, m = map(int, input().split())

graph = [[]*(n+1) for _ in range(n+1)]

for i in range(m):
    cmd = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[cmd[0]].append(cmd[1])
    graph[cmd[1]].append(cmd[0])

visited = [0]*(n+1)

def bfs(start):
    cnt = 0
    queue = deque([start])
    visited[start] = 1

    while(queue):
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i]=1
                queue.append(i)

result = 0
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        result += 1

print(result)
