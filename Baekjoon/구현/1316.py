# 2023/05/24
# 그룹 단어 체커

# import sys
# N = int(input())
# cnt = 0
# for _ in range(N):
#     cmd = sys.stdin.readline().rstrip()
#     alpha = []
#     last = ''
#     result = 1
#     for c in cmd:
#         if last == '':
#             last = c
#             alpha.append(c)
#         elif last == c:
#             last = c
#             continue
#         else:
#             if c not in alpha:
#                 last = c
#                 alpha.append(c)
#             else:
#                 result = 0
#     if result == 1 :
#         cnt += 1
# print(cnt)

N=int(input())
cnt=0
for i in range(N):
    word = input()  
    bl_=True
    for j in range(len(word)-1):
        if word[j]!=word[j+1]:
            if word[j] in word[j+1:]:
                bl_=False
                break
    if bl_:
        cnt+=1
print(cnt)