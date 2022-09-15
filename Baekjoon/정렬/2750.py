# 2022/09/14
# 수 정렬하기
# 오름차순 정렬


def sort(numList):
    numList.sort()
    for i in range(len(numList)):
        print(numList[i])

num_list=[]
N = int(input())
for i in range(N):
    num = int(input())
    num_list.append(num)
