# 2023/01/02
# 1463 : 1로 만들기

x = int(input())

# 최소 연산 횟수를 저장
dp = [0]*(x+1)
dp[1] = 1
dp[2] = 1

# bottom-up 방식
for num in range(1,x+1):
    cnt = 0
    num2 = num
    # 최소값을 찾기 위한 배열
    min_dp=[]

    if num2%3==0:
        num2=num2//3
        
    while(True):
        if dp[num2]>0:
            min_dp.append(dp[num2]+cnt)
            break

        if num2%3==0:
            num2=num2//3
        if num2%2==0:
            num2=num2//2
        else :
            num2=num2-1
        cnt += 1
    dp[num]=min(min_dp)

print(dp[x])