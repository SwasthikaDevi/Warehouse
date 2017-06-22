n=input("Enter a no.:")
q=n
sum=0
while(n>0):
    p=n%10
    sum=sum*10+p
    n=n/10
print(sum)

