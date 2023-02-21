# 2023/02/21
# 잃어버린 괄호

import sys

cmd = sys.stdin.readline().strip().split('-')
# 0으로 숫자 시작할 때 안됨
# result = eval(cmd[0]) 
# for num in cmd[1:]:
#     result -= eval(num)
# print(result)

result=0
cal_num = cmd[0].split('+')
new_num=0
for i in cal_num:
    new_num += int(i)
    result = new_num
for num in cmd[1:]:
    cal_num = num.split('+')
    new_num=0
    for i in cal_num:
        new_num += int(i)
    result -= new_num
print(result)
