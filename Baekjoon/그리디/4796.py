# 2023/01/30
# 캠핑

cnt = 0
while(True):
    cnt += 1
    result = 0
    date = list(map(int, input().split()))
    if (date[0]==0 and date[1]==0 and date[2]==0):
        break
    result=(date[2]//date[1])*date[0]
    if(date[2]%date[1]>=date[0]):
        result+=date[0]
    else:
        result+=date[2]%date[1]
    print("Case "+str(cnt)+": "+str(result))