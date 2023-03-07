# 2023/03/07
# 소가 길을 건너간 이유 1

import sys
N = int(input())
locations = [-1]*10
count = 0
for i in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    cow_num = int(cmd[0])-1
    cow_loc = int(cmd[1])
    if locations[cow_num]==-1:
        locations[cow_num]=cow_loc
    else:
        if locations[cow_num]!=cow_loc:
            count+=1
            locations[cow_num]=cow_loc
print(count)
