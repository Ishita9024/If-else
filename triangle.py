# ANGLES OF TRIANGLE

# a=int(input("enter the angle"))
# b=int(input("enter the angle"))
# c=int(input("enter the angle"))
# sum=a+b+c
# if sum==180 :
#     print("it is a valid triangle")
# else :
#     print("invalid")


# TYPES OF TRIANGLE

# a=int(input("enter the side"))
# b=int(input("enter the side"))
# c=int(input("enter the side"))
# if a==b==c :
#     print("equilateral")
# elif a==b or a==c or b==c :
#     print("isosceles")
# else :
#     print("scalene")
 
# SIDES

a=int(input("enter the side1"))
b=int(input("enter the side2"))
c=int(input("enter the side3"))
if a+b>c and  b+c>a and c+a>b :
    print("valid")
else :
    print("invalid")