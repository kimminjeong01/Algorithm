# 2023/04/16
# 통계학

import sys

N = int(sys.stdin.readline().rstrip())

nums = [0]*N

# 최빈값 구하기 위해
cnts = {}
for i in range(N):
    nums[i] = int(sys.stdin.readline().rstrip())
    
    if nums[i] in cnts:
        cnts[nums[i]] += 1
    else:
        cnts[nums[i]] = 1
        
# 최빈값 저장
max_dic = []
for i in cnts:
    if max(cnts.values()) == cnts[i]:
        max_dic.append(i)

# 산술 평균
print(round(sum(nums)/N))

# 중앙값
nums.sort()
print(nums[N//2])

# 최빈값
max_dic.sort()
if len(max_dic)>1:
    print(max_dic[1])
else:
    print(max_dic[0])

# 범위
print(nums[N-1]-nums[0])