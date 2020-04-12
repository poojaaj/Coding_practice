def containsDuplicate(num):
    j = 0
    val = False
    for i in range(1,len(nums)):
        while j != len(nums)-1 :
            if nums[i] == nums[j]:
            val = True
    return val

nums = [1,2,3,1]
print(containsDuplicate(nums))