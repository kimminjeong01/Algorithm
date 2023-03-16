# 2023/03/16
# 바이러스

import sys

# 컴퓨터의 수
num = int(input())

# 간선의 수
line = int(input())

# 그래프
graph = [[]*(num+1) for _ in range(num+1)]

# 방문처리
visited = [False]*(num+1)

for i in range(line):
    cmd = sys.stdin.readline().rstrip().split()
    x = int(cmd[0])
    y = int(cmd[1])
    graph[x].append(y)
    graph[y].append(x)

# dfs 함수
def dfs(graph, v, visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(visited.count(True)-1)

