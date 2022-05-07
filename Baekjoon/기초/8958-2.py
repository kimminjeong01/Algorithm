# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수
# OOXXOXXOOO => 1+2+0+0+1+0+0+1+2+3=10

num = int(input())
for i in range(num):
    strOX= input()
    score = 0 # O일 때 점수
    sum = 0   # 누적 점수
    for k in list(strOX):
        if k=='O':
            score += 1
            sum += score
        else :
            score =0
    print(sum)
