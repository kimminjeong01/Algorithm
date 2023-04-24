# 2023/04/14
# 부녀회장이 될테야

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    house = [[0]*n for _ in range(k+1)]
    for i in range(k+1):
        for j in range(n):
            if i==0:
                house[i][j] = j+1
            else:
                for l in range(j+1):
                    house[i][j] += house[i-1][l]
    print(house[k][n-1])
    
