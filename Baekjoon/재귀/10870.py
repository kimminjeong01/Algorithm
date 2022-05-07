# 2022/04/01
# 재귀 - 피보나치 수

def fibo(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    return fibo(num-1)+fibo(num-2)

num = int(input())
print(fibo(num))