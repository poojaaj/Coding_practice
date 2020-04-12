def revint(x):
    if x < 0:
        x = x * -1
        s = True
    else:
        s = False
    res = 0
    while x > 0:
        res = res * 10 + x % 10
        x = x // 10
        
    if s == True:
        res = res * -1
    return res

x = -120
print(revint(x))