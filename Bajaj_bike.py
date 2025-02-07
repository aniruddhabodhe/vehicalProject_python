# Bajaj_bike.py
def bajaj():
    print("-_" * 35)
    print("\t\t\t-:-WELCOME TO BAJAJ SHOWROOM-:-")
    print("-_" * 35)
    print("Bikes\t\t\tAmount")
    print("-" * 40)
    bikelist = {"pulsar n160": 122979,
                "pulsar 125": 86591,
                "chetak": 130596,
                "freedom": 93252,
                "dominar": 226069}
    avbike = {"pulsar n160": 5,
              "pulsar 125": 9,
              "chetak": 10,
              "freedom": 4,
              "dominar": 7}
    for k, v in bikelist.items():
        print(k, "--->Rs.", v)
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
                for key, value in avbike.items():
                    print(key, "\t\t", value)
            case "2":
                while True:
                    print("Add bikes You want")
                    bike = input("Enter bike name you want to purchase:")
                    if bike.lower() in bikelist and avbike[bike.lower()] > 0:
                        avbike[bike.lower()] -= 1
                        order_bike += bikelist[bike.lower()]
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
                        order_bike -= bikelist[item.lower()]
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
                    print(f"{a}\t\tRs.{bikelist[a]:.2f}")
                print("------------------------------")
                print(f"Total =>{order_bike:.2f}")
            case "5":
                print("**Thank you!_Visit Again 'BAJAJ' Showroom**")
                break
            case _:
                print("invalid choice----try again!")

