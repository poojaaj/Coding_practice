def helper(s,front,right):
    while right < len(s) and s[front] != s[right]:
        right = right + 1
    if right != len(s):
        return helper(s,front + 1, front +2)
    else:
        return front
def unique(s):
    front = 0
    right = 1
    return helper(s,front,right)
    
    
s = "leetcode"
print(unique(s))
