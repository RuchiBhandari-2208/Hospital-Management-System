from Hospitalsystem import hospitalsystem

hms=Hositalsystem()

while True:

    print("\n=====HOSPITAL MANAGEMENT SYSTEM======")
    print("1.Add patient")
    print("2.Display All Patient")
    print("3.Search Patient")
    print("4.Update Patient")
    print("5.Delete Patient")
    print("6.Exit")

    choice = input("Enter your choice:")

    if  choice == "1":
       hsm.add_patient()
    
    elif choice == "2":
        hms.display_patient()
    
    elif choice == "3":
        hms.search_patient()
    
    elif choice == "4":
       hms.update_patient()
    
    elif choice == "5":
        hms.delete_patient()
    
    elif choice == "6":
        print("Exit")
        break

    else:
        print("Invalid Choice.")
        
        


    