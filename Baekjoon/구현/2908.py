# 2023/05/03
# 상수

a, b = input().split()
newA = int(a[::-1])
newB = int(b[::-1])
if newA>=newB:
    print(newA)
else:
    print(newB)