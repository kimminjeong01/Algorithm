# 2023/04/02
# 경로 찾기

import sys
from collections import deque

N = int(input())

graph = [[]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    cmd = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(N):
        if cmd[j]==1:
            graph[i].append(j+1)


def bfs(start, end):
    result = 0
    visited = [False] * (N+1)
    queue = deque([start])

    while queue :
        q = queue.popleft()
        if start!=end:
            visited[q] = True

        for i in graph[q]:
            if not visited[i]:
                if i==end:
                    result = 1
                queue.append(i)
                visited[i] = True
    
    return result


for i in range(1,N+1):
    for j in range(1,N+1):
        print(bfs(i,j), end = ' ')
    print()
        
