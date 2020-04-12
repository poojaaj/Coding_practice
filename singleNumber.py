def singleNumber(nums):
    list = []
    for i in nums:
        if i in list:
            list.remove(i)
        else:
            list.append(i)
    return list.pop()
    

nums = [4,1,2,1,2]
print(singleNumber(nums))