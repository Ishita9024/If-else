day=input("enter the day")
if day=="thursday" :
    print("holiday")
    disco=input("grant permission")
    if disco=="yes" :
        print("allowed to go outside")
        place=input("enter the place")
        if place=="mall" :
            print("go")
            items=input("precautions items")
            if items=="mask and sanitizer" :
                print("ok")
                timings=input("enter the timings")
                if timings=="6 o'clock":
                    print("yes")
                else:
                    print("no")
        else:
            print("not go")
    else:
        print("not allowed")                
else:
    print("not a holiday")                
