# 2022/10/18
# 블로그 2

num = int(input())
str = list(input())

spl_str=1
for i in range(num-1):
    if str[i]!=str[i+1]:
        spl_str+=1

# +1은 전체 한번 칠한 것, spl_str//2는 R 연속된 개수
print(spl_str//2+1)

