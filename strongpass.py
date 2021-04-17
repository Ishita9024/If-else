num1=input("enter the alpha")
num2=input("enter the number")
num3=input("enter the special character")
num4=num1+num2+num3
if num1>="A" and num1<="Z" or num1>="a" and num1<="z" :
    if num2>="0" and  num2<="9" :
        if num3=="@" or num3=="#" or num3=="$" or num3=="&" :
            print(num4 , "it is a strong password")
        else :
            print("weak pass")
    else :
        print("weak password")                                               
else :
    print("weak")


# password=input("enter the password")
# if len(password)>=8 and len(password)<=16:
#     if "$" in password:
#         if "A" in password or "z" in password:
#             if "2" in password or "8" in password:
#                print("strong password")

#             else:
#                 print("weak password")
#         else:
#             print("weak password")      
#     else:
#         print("weak password")

# else:
#     print("weak password")
