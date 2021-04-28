print("Initializing system...")
print("Welcome")
print("ATM machine by rahimi")

# admin details 
admin = {"username" : "root", "pin" : 123456, "balance" : 0, "voidRecord" : 0}

# date innit
while True:
    date = input("Insert today date in (ddmmyy) format: ")
    if len(date) >= 7:
        print("Wrong format, system can't detect this format. Please re-enter date (ddmmyy).")
    elif len(date) <= 5:
        print("Wrong format, system can't detect this format. Please re-enter date (ddmmyy).")
    else: 
        print("System date set! Processing...")
        break

newDate = f"\n{date[0:2]}/{date[2:4]}/{date[4:]}"

# main loop
while True:
    print(newDate)
    print("---------") 
    print("(1) Charge card")
    print("(2) void")
    print("(3) Settlement")

    userInput = int(input())

    if userInput == 1:
        totalSale = int(input("Enter the total amount RM: "))
        print("(1) Swipe card")
        print("(2) Wave")
        wayOfCharge = int(input())
        if wayOfCharge == 1:
            print("Insert card..")
            print("Total RM: " + str(totalSale) + " charged.") 
            print("Take out card.")
            admin["balance"] += totalSale
        elif wayOfCharge == 2:
            print("Put card here")
            print(f"Card detected.. RM{totalSale} charged.")
            admin['balance'] += totalSale
    
    # void option
    elif userInput == 2:
        print("Enter admin username and PIN to proceed.")
        adminUsername = input("Username: \n")
        adminPIN = int(input("PIN: \n"))
        if adminUsername != admin["username"] and adminPIN != admin['pin']:
            print("Wrong username or PIN. Can't access void menu.")
        else:
            print("Warning!!!")
            print("All void amount will be return to customer account, void with care. ")
            voidAmount = int(input("Insert void amount: RM "))
            if voidAmount >= admin["balance"]:
                print('Error, the amount you enter is higher than your balance. Cancelling transaction.')
            else:
                admin['voidRecord'] += voidAmount
                print("Void success !!") 
            
        
    # settelement 
    elif userInput == 3:
        # ask permission before processing
        print("Are you sure want to print settlement ? Today record will be reset after settlement printed succesfully. (y/N): ")
        resetSettle = input()
        if resetSettle != 'y':
            pass # break after while loop
        else:
            print("Enter admin username and PIN to proceed.")
            adminUsername = input("Username: \n")
            adminPIN = int(input("PIN: \n"))
            if adminUsername != admin["username"] or adminPIN != admin['pin']:
                print("Wrong username or PIN. Cancelling settlement.")
            else:
                with open ("settelement.txt", "a") as file:
                    file.write("\nSETTLEMENT!\n")
                    file.write(f"Date : {date}.\n")
                    file.write(f"Total sales : RM{admin['balance']}.\n")
                    file.write(f"VOID amount: RM{admin['voidRecord']}.\n")
                    file.write("-------------------------------\n")

                print("Printing settlement...")
                print("Settlement printed succesfully, please re-login to start another transaction.")
                break
            


