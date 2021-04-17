num1 = int(input("enter any no."))
num2 = int(input("enter any no."))
num3=input("enter any symbol")
if num3=="+":
    print(num1+num2)
elif num3=="-":
    print(num1-num2)
elif num3=="*":
    print(num1*num2)
elif num3=="/":
    print(num2/num1)
elif num3=="%":
    print(num1%num2) 
elif num3=="**":
    print(num1**num2)
elif num3=="//":
    print(num1//num2)
else:
    print("invalid")


