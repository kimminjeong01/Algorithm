# 2023/05/09
# 절댓값 힙

# import sys
# import heapq

# N = int(sys.stdin.readline().rstrip())
# heap1 = [] # 양수
# heap2 = [] # 음수
# for i in range(N):
#     x = int(sys.stdin.readline().rstrip())
#     if x==0:
#         if not heap1:
#             if not heap2:
#                 print(0)
#             else:
#                 print(-heapq.heappop(heap2))
#         elif not heap2:
#             print(heapq.heappop(heap1))
#         else:
#             if heap1[0]>=heap2[0]:
#                 print(-heapq.heappop(heap2))
#             else:
#                 print(heapq.heappop(heap1))
#     elif x<0:
#         heapq.heappush(heap2,-x)
#     else:
#         heapq.heappush(heap1,x)

import heapq
import sys

n = int(input())
heap = []

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a!=0:
        heapq.heappush(heap,(abs(a),a))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])