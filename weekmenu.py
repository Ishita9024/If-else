day=input("enter the day")
menu=input("breakfast,lunch,dinner")
if day=="monday":
    if menu=="breakfast" :
        print("poha")
    elif menu=="lunch" :
        print("dal roti")
    else :
        print("pulao")
elif day=="tuesday":
    if menu=="breakfast" :
        print("sprouts")
    elif menu=="lunch" :
        print("roti sabzi")
    else :
        print("biryani")
elif day=="wednesday":
    if menu=="breakfast" :
        print("pasta")
    elif menu=="lunch" :
        print("chole bathure")
    else :
        print("daliya")
elif day=="thursday":
    if menu=="breakfast" :
        print("sabudana")
    elif menu=="lunch" :
        print("dal roti")
    else :
        print("rice")
elif day=="friday":
    if menu=="breakfast" :
        print("chilla")
    elif menu=="lunch" :
        print("rajma chawal")
    else :
        print("rajma roti")
elif day=="saturday":
    if menu=="breakfast" :
        print("macroni")
    elif menu=="lunch" :
        print("curd and aloo parantha")
    else :
        print("pulao")
else :
    print("choice")
