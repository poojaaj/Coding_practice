def removeDuplicate(l):
    i = 0
    for j in range(len(l)):
        if l[i]!= l[j]:
            i+=1
            l[i]=l[j]
    return i+1 


L = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicate(L))