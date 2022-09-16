# 2022/09/16
# 팰린드롬수
# 앞으로 읽어도 뒤로 읽어도 같으면 yes, 아니면 no

while(True):
    str1=input()
    if(str1=='0'):
        break
    str2=str1[::-1]
    if str1 == str2 :
        print("yes")
    else:
        print("no")