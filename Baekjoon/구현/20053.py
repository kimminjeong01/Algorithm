# 2023/03/03
# 최소, 최대 2

T = int(input())
for i in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    print(min(nums), max(nums))
