#2022/10/13
#좌표 정렬하기2

N = int(input())

arr=[]
for i in range(N):
    x,y =map(int,input().split())
    arr.append([y,x])
arr.sort()
for i in range(len(arr)):
    print(str(arr[i][1])+" "+str(arr[i][0]))

