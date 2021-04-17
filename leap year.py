num = int(input("enter any no"))
if num%4==0:
    if num%100==0:
        if num%400==0:
           print("it is a leap year")
        else:
            print("it is not a leap year")
    else:
        print("it's a leap year")
else:
    print("it is not a leap year")      
      
