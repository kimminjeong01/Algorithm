# 2022/10/30
# 셀프 넘버

selfNum = 1
while selfNum<=10000:
    print(selfNum)
    new = selfNum
    selfNum += new // 1000
    new%=1000
    selfNum += new // 100
    new%=100
    selfNum += new // 10
    new%=10
    selfNum += new
