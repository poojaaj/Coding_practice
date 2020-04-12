# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

# Example 1:

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
a = ["h","e","l","l","o"]
    
def reverse_str(a):
    front = 0
    back = len(a)-1
    while front < back:
        a[front] ,a[back] = a[back] , a[front]
        front = front + 1
        back = back - 1
    return a

print(reverse_str(a))