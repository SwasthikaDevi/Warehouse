n=input("Enter a no.:")
q=n
s=0
while(n>0):
    p=n%10
    s=s*10+p
    n=n/10
if(s==q):
    print("The no. is palindrome")
else:
    print("The no. is not a palindrome")
