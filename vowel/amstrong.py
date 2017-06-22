n=input("Enter a no.:")
s=0
q=n
while(n>0):
    p=n%10
    s+=p*p*p
    n=n/10
print(s)
if(s==q):
    print("It's amstrong no:")
