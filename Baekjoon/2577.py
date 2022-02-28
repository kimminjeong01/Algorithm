# 곱셈 결과에 각각의 숫자가 몇번씩 쓰였는지

a= int(input())
b= int(input())
c= int(input())

mul = a*b*c

for i in range(10):
    cnt=str(mul).count(str(i))
    print(cnt)


