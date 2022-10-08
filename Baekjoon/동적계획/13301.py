# 2022/10/08
# 타일 장식물

num = int(input())

numList=[0]*(num+2)
numList[1]=1
numList[2]=1

def count(n):
    for i in range(3,n+1):
        if numList[i]==0:
            numList[i]=count(i-1)+count(i-2)
    return numList[n]

print(2*(2*count(num)+count(num-1)))