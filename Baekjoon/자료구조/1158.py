# 2022/09/25
# 요세푸스 문제

from collections import deque

x, y = map(int,input().split())

queue= deque()
print_queue=deque()
for i in range(x):
    queue.append(i+1)

index=0
while(True):
    if len(queue)==0:
        break
    index+=y-1
    if(index>=len(queue)):
        index = index % len(queue)
    print_queue.append(queue[index])
    queue.remove(queue[index])

print("<", ', '.join(str(i) for i in print_queue), ">", sep="")


# n, k = map(int, input().split())
# arr = [i for i in range(1, n + 1)]
# answer = []
# num = k - 1

# for i in range(n):
#     if len(arr) > num:
#         answer.append(arr.pop(num))
#         num += k - 1
#     elif len(arr) <= num:
#         num = num % len(arr)
#         answer.append(arr.pop(num))
#         num += k -1
        
# print("<", ', '.join(str(i) for i in answer), ">", sep = '')