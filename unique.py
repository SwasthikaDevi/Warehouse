n=input("Enter the no. of array elements:")
c=list()
out=list()
check=0
for i in range(n):
    x=input("Enter an element:")
    c.append(x)
    out.append(0)
for i in c:
    if c.count(i)==1:
        print(i)
