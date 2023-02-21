# 2023/01/31
# 소수 구하기

m, n = map(int, input().split())

# # 시간 초과
# for i in range(m, n+1):
#     cnt = 0
#     for j in range(2,i):
#         if i%j==0:
#             break
#         cnt +=1
#     if cnt==i-2:
#         print(i)
        
# 에라토스테네스의 체
for i in range(m, n+1):
    if i==1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            break
    else:
        print(i)