# 
# 후위 표기식 2

cnt = int(input())
cal = list(input())

for i in range(cnt):
    num = int(input())
    cal[cal.index(chr(65+i))] = num
