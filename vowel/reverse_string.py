string=raw_input("Enter a string:")
word=string.split()
str=""
for i in word[::-1]:
    str+=" "+i
print(str)
