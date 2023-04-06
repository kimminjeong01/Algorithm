# 2023/04/06
# 피보나치 함수

# # 시간초과
# import sys

# def fibonacci(n):
#     if (n==0):
#         cnt[0]+=1
#         return 0
#     elif (n==1):
#         cnt[1]+=1
#         return 1
#     else :
#         return fibonacci(n-1)+fibonacci(n-2)
    
# n = int(sys.stdin.readline().rstrip())
# for _ in range(n):
#     cnt = [0,0]
#     num = int(sys.stdin.readline().rstrip())
#     fibonacci(num)
#     for i in cnt:
#         print(i, end=' ')
#     print()

def fib(n):
    zeros = [1,0,1]
    ones = [0,1,1]

    if n>=3:
        for i in range(2, n):
            zeros.append(zeros[i-1]+zeros[i])
            ones.append(ones[i-1]+ones[i])
    print(f"{zeros[n]} {ones[n]}")

N = int(input())
for _ in range(N):
    num = int(input())
    fib(num)