# 2023/02/01
# 좌표 압축

# #시간초과
# n = int(input())
# nums = list(map(int, input().split()))
# nums_sort = nums.copy()
# nums_sort.sort()

# for num in nums:
#     result = 0
#     for check_num in nums_sort:
#         if num>check_num:
#             result +=1
#         else:
#             break
#     print(result,end=" ")

# 자신이 리스트 안에서의 크기 순서를 출력하면 됨
# 딕서녀리 : 시간복잡도 O(1)
import sys
n = int(input())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

numset = set(numbers)
a = list(numset)
a.sort()

numdict = {}
for i in range(len(a)):
    numdict[a[i]] = i

for i in numbers:
    print(numdict[i], end=' ')
