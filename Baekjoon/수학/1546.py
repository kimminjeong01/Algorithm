# 2022/10/22
# 평균

n = int(input())
nums = list(map(int,input().split()))
maxNum=max(nums)
for i in range(n):
    nums[i]=nums[i]/maxNum*100
print(sum(nums)/n)