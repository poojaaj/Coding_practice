#Given an integer n and an integer start.

#Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

#Return the bitwise XOR of all elements of nums.



def xorOperation(n, start):
    nums = []
    xor_arr = 0
    for i in range(n):
        nums.append(start + 2*i)
    print(nums)
    for i in nums:
        xor_arr = xor_arr ^ i
    print(xor_arr)


n = 5
start = 0

xorOperation(n, start)
