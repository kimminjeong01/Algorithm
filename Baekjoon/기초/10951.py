# a와 b를 입력받아 더한 값 출력
# 예외 처리

while(1):
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
