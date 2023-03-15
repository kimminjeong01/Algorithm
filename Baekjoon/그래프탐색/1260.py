# 2023/03/15
# DFS와 BFS

import sys
from collections import deque

N, M, V = map(int, input().split())

# 그래프
graph = [[] * (N + 1) for _ in range(N + 1)] 
for i in range(M):
    cmd = sys.stdin.readline().rstrip().split()
    graph[int(cmd[0])].append(int(cmd[1]))
    graph[int(cmd[1])].append(int(cmd[0]))

for gr in graph :
    gr.sort()

# 방문 처리
visited_dfs = [False]*(N+1)
visited_bfs = [False]*(N+1)

# dfs
def dfs(graph, V, visited_dfs):
    visited_dfs[V] = True
    print(V, end=' ')

    for i in graph[V]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)

# bfs
def bfs(graph, V, visited_bfs):
    queue = deque([V])
    visited_bfs[V] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

# 출력
dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)

