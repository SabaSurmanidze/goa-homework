day = input("enter day")
hour = int(input("enter hour"))

if day == "monday":
    print("open")
elif day == "tuesday":
    print("open")
elif day == "wednesday":
    print("open")
elif day == "thursday":
    print("open")
elif day == "friday":
    print("open")
elif day == "saturday":
    print("close")  
elif day == "sunday":
    print("close") 
elif hour <=21:
    print("open")
elif hour >=11:
    print("open")
else:
    print("close")
    
    
