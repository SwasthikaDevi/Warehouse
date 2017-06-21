string=raw_input("Enter the string:")
r=string.split(" ")
s=""
for i in (r[::-1]):
    s+=" "+i
print (s)
