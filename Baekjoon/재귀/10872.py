# 2022/03/31
# 재귀 - 팩토리얼 

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

num= int(input())
print(factorial(num))