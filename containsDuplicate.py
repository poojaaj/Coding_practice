def containsDuplicate(nums):
    if len(set(nums)) != len(nums):
        return True
    else:
        return False

nums = [2,14,18,22,22]
print(containsDuplicate(nums))


#altrnative method
# def containsDuplicate(nums):
#     l = []
#     for i in nums:
#         if i not in l:
#             l.append(i)
#     if len(l) != len(nums):
#         return True
#     else:
#         return False

# nums = [1,2,3,4]
# print(containsDuplicate(nums))
