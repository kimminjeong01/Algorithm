# 2023/05/02
# 빙고

import sys

bingo = []
speak = []
for _ in range(5):
    cmd = list(map(int,sys.stdin.readline().rstrip().split()))
    bingo.append(cmd)

for _ in range(5):
    cmd = list(map(int,sys.stdin.readline().rstrip().split()))
    speak.append(cmd)

result = 0
def check(bingo):
    cnt = 0

    # 가로
    for i in range(5):
        sum = 0
        for j in range(5):
            sum += bingo[i][j]
        if sum==0:
            cnt += 1
    
    # 세로
    for i in range(5):
        sum = 0
        for j in range(5):
            sum += bingo[j][i]
        if sum==0:
            cnt += 1
    
    # 대각선
    sum = 0
    for i in range(5):
        sum += bingo[i][4-i]
    if sum == 0:
        cnt += 1
    
    sum = 0
    for i in range(5):
        sum += bingo[i][i]
    if sum == 0:
        cnt += 1
    
    return cnt

            
for i in range(5):
    for j in range(5):
        now = speak[i][j]
        
        for m in range(5):
            for n in range(5):
                if now == bingo[m][n]:
                    bingo[m][n] = 0
                    result = check(bingo)
                    if result>=3:
                        print(i*5 + j+1)
                        exit()
                    continue     