# 2023/01/24
# 숫자 카드

# 시간 초과
# N = int(input())
# cards = list(map(int,input().split()))
# M = int(input())
# nums = list(map(int,input().split()))

# for num in nums:
#     if num in cards:
#         print(1, end=" ")
#     else:
#         print(0,end=" ")

N = int(input())
# 집합
cards = set(map(int,input().split()))
M = int(input())
nums = list(map(int,input().split()))

for i in range(M):
    if nums[i] in cards:
        print(1, end=" ")
    else:
        print(0,end=" ")


# # 이진탐색으로 풀기
# import sys

# N = int(sys.stdin.readline())
# cards = sorted(list(map(int, sys.stdin.readline().split())))
# M = int(sys.stdin.readline())
# checks = list(map(int, sys.stdin.readline().split()))

# for check in checks:
#     low, high = 0, N-1  # cards의 이진 탐색 index
#     exist = False
#     while low <= high:
#         mid = (low + high) // 2
#         if cards[mid] > check:  # 중간 값보다 작다면
#             high = mid - 1  # 중간보다 왼쪽 한 칸 옆까지 탐색
#         elif cards[mid] < check:  # 중간 값보다 크다면
#             low = mid + 1  # 중간보다 오른쪽 한 칸 옆부터 탐색
#         else:
#             exist = True
#             break
#     print(1 if exist else 0, end=' ')