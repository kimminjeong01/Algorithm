# 2022/10/08
# 단어공부

# word = input()
# countList=[0]*26

# for i in word:
#     ascii = ord(i)
#     if ascii>=65 and ascii<=90:
#         countList[ascii-65]+=1
#     elif ascii>=97 and ascii<=122:
#         countList[ascii-97]+=1

# maxIndex = 0
# for i in range(len(countList)):
#     if countList[maxIndex]<=countList[i]:
#         maxIndex=i

# if countList.count(max(countList))>1:
#     print("?")
# else :
#     print(chr(maxIndex+65))


word = input()
countList=list(set(word))
cnt = []
print(countList)

for i in countList:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt))>=2:
    print("?")
else:
    print(countList[(cnt.index(max(cnt)))].upper())