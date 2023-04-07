# 2023/04/07
# 듣보잡

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

nolisten = set()
nowatch = set()

for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    nolisten.add(cmd)

for _ in range(M):
    cmd = sys.stdin.readline().rstrip()
    nowatch.add(cmd)

nolisten_watch = nolisten & nowatch
print(len(nolisten_watch))
for str in sorted(nolisten_watch):
    print(str)
