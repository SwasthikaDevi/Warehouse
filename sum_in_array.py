g=list()
c=0

n=input("Enter the no. of elements:")
for i in range(n):
    e=input("Enter an element:")
    g.append(e)
s=input("Enter the sum element:")
for i in range(n-1):
    for j in range(n):
        if g[i]+g[j]==s:
            ans=g[i]
            an2=g[j]
            c=1
            break
if c==1:
    print("Yes,it is present")
    print(ans,an2)
else:
    print("No,its not there")
