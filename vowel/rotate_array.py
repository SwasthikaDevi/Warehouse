n=input("Enter the no of elements:")
c=list()
for i in range(n):
    e=input("Enter the no of elements:")
    c.append(e)
t=input("Enter the no. of rotations:")
for j in range(t):
    v=c[n-1]
    for i in range(n-2,-2,-1):
        p=c[i]
        c[i]=v
        v=p
print(c)
