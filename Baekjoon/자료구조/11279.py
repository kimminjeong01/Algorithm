# 2023/05/06
# 최대 힙

import heapq
import sys

N = int(sys.stdin.readline().rstrip())
heap=[]
for i in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x==0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap,-x)
