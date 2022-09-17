# 2022/09/17
# 좌표 정렬하기

# 입력
N = int(input())
point_list= []
for i in range(N):
    point = list(map(int, input().split()))
    point_list.append(point)

# 정렬
point_list.sort()

for i in range(N):
    print("{0} {1}".format(point_list[i][0],point_list[i][1]))

