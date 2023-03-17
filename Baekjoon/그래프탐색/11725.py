# 2023/03/17
# 트리의 부모 찾기

import sys
from collections import deque

num = int(input())

graph=[[]*(num+1) for _ in range(num+1)]
for i in range(num-1):
    cmd = list(map(int,sys.stdin.readline().rstrip().split()))
    graph[cmd[0]].append(cmd[1])
    graph[cmd[1]].append(cmd[0])

visited = [False]*(num+1)
parents = [0]*(num+1)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v]=True

    while queue:
        parent= queue.popleft()
        for i in graph[parent]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                parents[i]=parent

bfs(graph, 1, visited)

for parent in parents[2:]:
    print(parent)


