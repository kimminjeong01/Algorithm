# 2022/10/10
# 설탕배달

num = int(input())

cnt = 0

while(num!=0):
    if num%5==0:
        cnt+=num//5
        num =0
    elif num>0:
        cnt +=1
        num -=3
    elif num<0:
        cnt=-1
        break
print(cnt)