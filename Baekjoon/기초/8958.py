# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수
# OOXXOXXOOO => 1+2+0+0+1+0+0+1+2+3=10

num = int(input())
for i in range(num):
    strOX= input()
    before = False # 이전의 값이 O이면 True, X이면 False
    con = 0 # 연속된 값 개수
    score = 0
    for k in list(strOX):
        if k=='O':
            con += 1
            if before == True :
                score = score + con
            else: 
                score += 1
            before = True
        else :
            con =0
            before = False
    print(score)
        

