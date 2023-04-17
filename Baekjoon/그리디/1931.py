# 2023/04/17
# 회의실 배정

import sys
N = int(sys.stdin.readline().rstrip())
meetings = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    meetings.append((start, end))
meetings.sort(key = lambda x:(x[1], x[0]))

result = 0
now = 0
for meeting in meetings:
    if now <= meeting[0]:
        now = meeting[1]
        result += 1
print(result)