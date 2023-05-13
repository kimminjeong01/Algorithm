# 2023/05/11
# 킹

import sys

cmd = sys.stdin.readline().rstrip().split()

N = int(cmd[2])

x = int(cmd[0][1])-1
y = ord(cmd[0][0])-65

x2 = int(cmd[1][1])-1
y2 = ord(cmd[1][0])-65

for i in range(N):
    cmd = sys.stdin.readline().rstrip()
    if cmd =="R":
        if 0<=y+1<8:
            y += 1
            if x==x2 and y==y2:
                if 0<=y2+1<8:
                    y2 += 1
                else:
                    y -= 1
    elif cmd =="L":
        if 0<=y-1<8:
            y -= 1
            if x==x2 and y==y2: 
                if 0<=y2-1<8:
                    y2 -= 1
                else:
                    y += 1
    elif cmd == "B":
        if 0<=x-1<8:
            x  -= 1
            if x==x2 and y==y2: 
                if 0<=x2-1<8:
                    x2 -= 1
                else:
                    x+=1
    elif cmd == "T":
        if 0<=x+1<8:
            x += 1
            if x==x2 and y==y2 :
                if 0<=x2+1<8:
                    x2 += 1
                else:
                    x -= 1
    elif cmd == "RT":
        if 0<=x+1<8 and 0<=y+1<8:
            x += 1
            y += 1
            if x==x2 and y==y2 :
                if 0<=x2+1<8 and 0<=y2+1<8:
                    x2 += 1
                    y2 += 1
                else:
                    x -= 1
                    y -= 1
    elif cmd == "LT":
        if 0<=x+1<8 and 0<=y-1<8:
            x += 1
            y -= 1
            if x==x2 and y==y2 :
                if 0<=x2+1<8 and 0<=y2-1<8:
                    x2 += 1
                    y2 -= 1
                else:
                    x -= 1
                    y += 1
    elif cmd =="RB":
        if 0<=x-1<8 and 0<=y+1<8:
            x -= 1
            y += 1
            if x==x2 and y==y2 :
                if 0<=x2-1<8 and 0<=y2+1<8:
                    x2 -= 1
                    y2 += 1
                else:
                    x += 1
                    y -= 1
    elif cmd =="LB":
        if 0<=x-1<8 and 0<=y-1<8:
            x -= 1
            y -= 1
            if x==x2 and y==y2: 
                if 0<=x2-1<8 and 0<=y2-1<8:
                    x2 -= 1
                    y2 -= 1
                else:
                    x += 1
                    y += 1
  
print(chr(y+65)+str(x+1))
print(chr(y2+65)+str(x2+1))
