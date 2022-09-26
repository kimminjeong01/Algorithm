# 2022/09/26
# 에라토스테네스의 체


x, y = map(int, input().split())
arr = [False] * (x-1)
cnt = 0
for i in range(len(arr)):
    if arr[i]==False:
        for j in range(i,len(arr)):
            if (j+2)%(i+2)==0 :
                if arr[j]==False:
                    arr[j]=True
                    cnt +=1
                    if cnt == y:
                        print(j+2)
                        break


