balance = 1000  # Initial balance

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is:", balance)
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposited {amount}. New balance is {balance}")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            print(f"Withdrawn {amount}. New balance is {balance}")
    elif choice == "4":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")