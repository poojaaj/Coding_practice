a = []
sum = 0
for i in range(1000):
    if i % 3 == 0:
        a.append(i)
        sum = sum + i
    elif i % 5 == 0:
        a.append(i)
        sum = sum + i
print(a)
print(sum)