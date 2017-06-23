def circle(r):
    return 3.14*(r**2)
def rectangle(l,b):
    return l*b
def triangle(b,h):
    return 1.5*b*h
print ("1.Circle\n2.Rectangle\n3.Square")
ch=input("Enter your choice:")
if (ch==1):
    r=input("Enter the radius:")
    print("Area of circle:"+str(circle(r)))
if (ch==2):
     l=input("Enter the breadth:")
     b=input("Enter the height:")
     print("Area of rectangle:"+str(rectangle(l,b)))
if (ch==3):
     b=input("Enter the base:")
     h=input("Enter the height:")
     print("Area of triangle:"+str(triangle(b,h)))
