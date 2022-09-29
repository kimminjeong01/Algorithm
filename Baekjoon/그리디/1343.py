# 2022/09/29
# 폴리오미노

board=list(map(str,input().split('.')))
result=''
for x in range(len(board)):
    xs=board[x]
    if len(xs)%2!=0:
        result=-1
        break
    else:
        cnt = len(xs)
        while(cnt>0):
            if cnt>=4:
                result += 'AAAA'
                cnt-=4
            else: 
                result +='BB'
                cnt -=2
        if x!=len(board)-1:
            result+='.'

print(result)
    

# # replace 사용             
# board = input()

# board = board.replace("XXXX","AAAA")
# board = board.replace("XX","BB")

# if 'X' in board:
#     print(-1)
# else :
#     print(board)

