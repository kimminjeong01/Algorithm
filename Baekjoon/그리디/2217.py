# 2022/10/01
# 로프
# k개의 로프를 이용하여 중량이 w인 물체를 들어올릴 때,
# 모두 고르게 w/k 만큼의 중량이 걸리게 됨
# 최대 중량 구하기

# N = int(input())
# rope = [int(input()) for _ in range(N)]
# rope.sort()
# # 모두 다 사용
# max = rope[0]*len(rope)
# rope.pop(0)
# while(True):
#     if len(rope)==0:
#         break
#     # 가장 작은 것을 뺀 경우
#     elif max<rope[0]*len(rope):
#         max = rope[0]*len(rope)  
#     rope.pop(0)
# print(max)


N = int(input())
rope =[]
value = []
for i in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)
for num in range(N):
    #rope[n]*n번째 자리
    value.append(rope[num]*(num+1))
print(max(value))
