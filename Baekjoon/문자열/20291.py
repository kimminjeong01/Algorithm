# 2023/04/23
# 파일 정리

import sys

N = int(sys.stdin.readline().rstrip())

files = dict()
for i in range(N):
    cmd = list(sys.stdin.readline().rstrip().split("."))
    if cmd[1] not in files.keys():
        files[cmd[1]] = 1
    else:
        files[cmd[1]] += 1
    

for f in sorted(files):
    print(f+" "+str(files[f]))


