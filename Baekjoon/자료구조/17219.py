# 2023/03/30
# 비밀번호 찾기

import sys

# 저장된 사이트 주소의 수, 비밀번호를 찾으려는 사이트 주소의 수
n, m = map(int, sys.stdin.readline().rstrip().split())

dict = {}
for i in range(n):
    cmd = sys.stdin.readline().rstrip().split()
    dict[cmd[0]] = cmd[1]

for j in range(m):
    cmd = sys.stdin.readline().rstrip()
    print(dict[cmd])