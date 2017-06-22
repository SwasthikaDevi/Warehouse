count=0
n=input("Enter the no.:")
while(n>0):
    if n%10!=0 :
        count+=1
    n=n/10
print(count)
