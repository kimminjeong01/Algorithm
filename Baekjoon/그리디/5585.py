# 2022/10/15
# 거스름돈

back = 1000-int(input())
cnt = 0
while(True):
    if back>=500:
        cnt += back//500
        back = back%500
    elif back>=100:
        cnt += back//100
        back = back%100
    elif back>=50:
        cnt += back//50
        back = back%50
    elif back>=10:
        cnt += back//10
        back = back%10
    elif back>=5:
        cnt += back//5
        back = back%5
    else:
        cnt += back
        back = 0
        break
print(cnt)