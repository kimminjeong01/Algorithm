# 2022 /09 /15
# 직사각형에서 탈출하기

num_list = list(map(int, input().split()))

check_list = []
check_list.append(abs(num_list[2]-num_list[0]))
check_list.append(abs(num_list[3]-num_list[1]))
check_list.append(abs(num_list[0]-0))
check_list.append(abs(num_list[1]-0))
check_list.sort()
print(check_list[0])
