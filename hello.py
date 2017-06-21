a=list()
out=list()
n=input("Enter the no .of element:")
for i in range(n):
    r=input("Enter an element:")
    out.append(0)
    a.append(r)
for i in range(n):
    if(a.count(a[i])>1):
        if(out[a.index(a[i])]==0):
            print(a[i])
            for j in range(n):
                if(a[j]== a[i]):
                    out[j]=1
