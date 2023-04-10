# 2023/04/10
# 방 번호

num = input()
nums = [0]*10
for i in num:
    if(int(i)==9 or int(i)==6):
        # 6과 9를 동일하게 취급
        if nums[6]<nums[9]:
            nums[6]+=1
        else:
            nums[9]+=1
    else:
        nums[int(i)]+=1

print(max(nums))

