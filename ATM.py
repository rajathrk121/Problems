balance=1000
print("1 For Deposit \n2 For Withdraw \n3 For Check Balance \n4 For Exit")
choice=int(input("Enter your choice: "))



if choice==1:
    dep=int(input("Enter Deposit Amount: "))
    balance+=dep
    print("Amount",dep ,"deposited successfully")
    print("Current Balance:",balance)


elif choice==2:
    withd=int(input("Enter withdraw amount: "))
    if withd<=balance:
        balance-=withd
        print(withd,"withdrawn successfully")
        print("Current Balance:",balance)
    else:
        print("Insufficient Balance")


elif choice==3:
    print("Your Account Balance is:",balance)


elif choice==4:
    exit()


else:
    print("Invalid choice")
