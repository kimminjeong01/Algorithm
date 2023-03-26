# 2023/03/23
# 특정 거리의 도시 찾기

import sys
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
n, m, k, x = map(int, input().split())

# 그래프
graph = [[]*(n+1) for _ in range(n+1)]
visited=[-1]*(n+1)

for i in range(m):
    cmd = list(map(int,sys.stdin.readline().rstrip().split()))
    graph[cmd[0]].append(cmd[1])

def bfs(s, visited):
    visited[s]=0
    queue = deque([s])

    while(queue):
        now = queue.popleft()
        
        for next in graph[now]:
            if visited[next]==-1:
                queue.append(next)
                visited[next]=visited[now]+1

bfs(x, visited)

# 결과 출력
cnt = 0
for i in range(1,n+1):
    if visited[i]==k:
        print(i)
    else:
        cnt+=1
if(cnt==n):
    print(-1)





