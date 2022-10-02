# 2022/10/02
# 카드2

from collections import deque

N = int(input())
card = deque()
for i in range(N):
    card.append(i+1)

while(len(card)!=1):
    card.popleft()
    card.append(card[0])
    card.popleft()
print(card[0])

