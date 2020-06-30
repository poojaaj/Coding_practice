def shuffle(nums, n):
    l = []
    j = n
    for i in range(0,n):
        l.append(nums[i])
        l.append(nums[j])
        j += 1
    return l
nums = [2, 5, 1,3,4,7]
n = 3
print(shuffle(nums, n))
