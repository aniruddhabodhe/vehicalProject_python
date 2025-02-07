# vehical_main.py
from Honda_bikes import honda
from Bajaj_bike import bajaj
from Yamaha_bikes import yamaha
while True:
    vehicals='''------------------------------------------
        Select Company name to visite: 
    ----------------------------------------------
                1.Honda 
                2.Bajaj
                3.Yamaha
                4.Exist'''
    print("-"*40)
    print(vehicals)
    ch=input("Enter choice(1-4):")
    match(ch):
        case "1":
            honda()
        case "2":
            bajaj()
        case "3":
            yamaha()
        case "4":
            print("*"*30)
            print("\t**Thank You..Visit Again!**")
            print("*"*30)
            break
        case _:
            print("Invalid Choice....Try Again!")
