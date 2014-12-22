import math

def tri(n):
    return ((n+1)*(n)/2)

for i in range(7,1000000):
    l=[]
    l.append(1)
    l.append(tri(i))
    for j in range(2,int(math.sqrt(tri(i)))+1):
        if(not tri(i)%j):
            l.append(j)
            l.append(tri(i)/j)
    if(len(l)>500):
        print(i)
        print (tri(i))
        break

