# 2022/10/19
# 수 정렬하기 3

# sort 쓰면 메모리 초과
# 계수 정렬

import sys

num = int(input())
arr = [0]*10001
for i in range(num):
    arr[int(sys.stdin.readline())]+=1

for i in range(1,len(arr)):
    if arr[i]!=0:
       for j in range(arr[i]):
            print(i) 
