# 2022/06/28
# 블랙잭
# 모든 경우의 수를 다 뒤져봐야하는 완전 탐색 문제
# from itertools import combinations로 조합을 사용하는 방법도 있음

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

def blackjack(N,M):
    max=0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                total=num_list[i]+num_list[j]+num_list[k]
                if total>max and total<=M:
                    max=total
         
    print(max)

blackjack(N,M)



