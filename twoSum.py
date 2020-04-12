# def twoSum(n,t):
#     front = 0
#     right = 1
#     for i in range(len(n)):
#         if n[front]+n[right] == t:
#             return front,right

def twoSum(nums, target):
        lookup = {}
        for index, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target-num], index
            lookup[num] = index

n = [2,7,11,15]
target = 9
print(twoSum(n,target))
