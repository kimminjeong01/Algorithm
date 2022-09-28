# 2022/09/28
# 거스름돈

money = int(input())

cnt =0
while(money>0):
    if (money % 5 ==0):
        # 5로 나눠지면 다 5원으로
        money -=5
        cnt +=1
    else :
        # 안나눠지면 2원으로
        money -=2
        cnt +=1

# 음수가 나오면 거슬러 줄 수 없음
if money<0:
    print(-1)
else :
    print(cnt)



# 5원으로 다 바꾸고 2원하려 했는데 안됨