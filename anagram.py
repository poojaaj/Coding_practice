s = "ee"
t = "rr"
x = sorted(s)
y = sorted(t)
if len(s) != len(t):
    print("false")
else:
    for i in range(len(x)):
        if x[i] != y[i]:
            print("false")
        else:
            print("true") 