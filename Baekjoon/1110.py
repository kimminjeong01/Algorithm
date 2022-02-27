num = int(input())
new_num=num
cnt=0
while True:
    a = new_num%10
    b = new_num//10

    b = (a+b)%10
    new_num = a*10 +b
    cnt+=1
    if new_num==num:
        break;
print(cnt)
