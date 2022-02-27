# 별찍기

num = int(input())

for i in range(num):
    for j in range(num-i-1):
        print(' ', end='')
    if i==0:
        print('*', end='')
    elif i==num-1:
        for k in range(2*(i+1)-1):
            print('*', end='')
    else:
        print('*', end='')
        for k in range(2*i-1):
            print(' ', end='')
        print('*', end='')
    print()

# 반복문 말고 문자열 '*' 사용해보기