n=input("Enter the no. of terms:")
i=0
a=-1
b=1
if(n>0):
    while i<n:
        c=a+b
        print (c)
        a=b
        b=c
        i+=1
else:
    print("Give +ve no. of terms:")
