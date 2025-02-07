# Yamaha_bikes.py
def yamaha():
    print("-_" * 35)
    print("\t\t-:-Welcome YAMAHA BiKE SHOWROOM -:-")
    print("-_" * 35)
    print("Menu =>")
    menu = {"yamaha mt15v2": 170064,
            "yamaha r15v4": 184459,
            "yamaha fzsf1v4": 131284,
            "yamaha rayzr": 87888,
            "yamaha fzsf1": 123484,
            "yamaha mt03": 460639}
    print("Bike name\t\t\tRs.")
    avbike = {"yamaha mt15v2": 0,
              "yamaha r15v4": 3,
              "yamaha fzsf1v4": 6,
              "yamaha rayzr": 12,
              "yamaha fzsf1": 10,
              "yamaha mt03": 8}
    for k, v in menu.items():
        print(k, "--->", v)
    print("-------------------------------------")
    print("1.Available_Bikes\n2.ADD BiKE\n3.REMOVE BIKE\n4.Bill Rrecipt\n5.Exist")
    print("-------------------------------------")
    order_bike = 0
    lst = []
    while True:
        ch = input("Enter your choice(1-5):")
        print("-------------------------------------")
        match ch:
            case "1":
                print("-:-Check_Available_Bikes-:-")
                print("------------------------------")
                print("BiKE\t\tAvailable_BIke")
                for key,value in avbike.items():
                    print(key,"\t\t",value)
            case "2":
                while True:
                    print("Add bikes You want")
                    bike = input("Enter bike name you want to purchase:")
                    if bike.lower() in menu and avbike[bike.lower()] >0:
                        avbike[bike.lower()]-=1
                        order_bike += menu[bike.lower()]
                        lst.append(f"{bike.lower()}")
                        print(f"'{bike}' BiKE is added")
                    else:
                        print("Bike is not available")
                    ch = input("If you want add another BiKE(YES/NO):")
                    if ch.lower() == "no":
                        break
                print("--------------------------")
                print("-:-BiKEs ADD liST-:-")
                print("--------------------------")
                for k in lst:
                    print(k)

                print("------------------------------------------------------")
                print("------------------------------------------------------")
            case "3":
                while True:
                    print("Remove bikes")
                    item = input("Enter BiKE Name You Want To Remove:")
                    if item.lower() in lst:
                        # lst.remove(f"ip;{bike.lower()}\tRs.{menu[bike.lower()]}")
                        avbike[item.lower()] += 1
                        order_bike -= menu[item.lower()]
                        lst.remove(item)
                        print("remove")
                        print("-------------------------------")
                    else:
                        print(f"{item} BiKE is not in add list")
                    ch = input("Do you want remove another BiKE(YES/NO):")
                    if ch.upper() == "NO":
                        break
                print("--------------------------")
                print("-:-BiKEs ADD liST-:-")
                print("--------------------------")
                for k in lst:
                    print(k)
                print("------------------------------------------------------")
                print("------------------------------------------------------")
            case "4":
                print("-_" * 35)
                print("\t\t-:-Bill Receipt-:-")
                print("-_" * 35)
                print("BiKEs\t\t\t\tAmount.")
                for a in lst:
                    print(f"{a}\t\tRs.{menu[a]:.2f}")
                print("------------------------------")
                print(f"Total =>{order_bike:.2f}")
            case "5":
                print("Thank you!_Visit Again")
                break
            case _:
                print("invalid choice----try again!")

