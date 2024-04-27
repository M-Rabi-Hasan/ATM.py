condition = True    
condition1 = True

while condition1:
    max_attempts = 3
    attempts = 0
   
    try:
        my_account_balance: int = 10000
        my_pin: int = 1234

        while  attempts < max_attempts:
            pin = input("Enter your pin: ")

            if int(pin) == my_pin:  
                print("Your pin is correct")
                condition1 = False
                break
                
            else:
                print("Invalid pin")
                attempts += 1

            if attempts == max_attempts:
                print("Too many incorrect attempts. Your account is locked.")
                break
            
                
    except ValueError:
        print("Please enter a numeric pin.")



while condition:
    try:
            print("What do you want?\nCheck balance, Deposit, Withdraw, Logout: ")
            operation = input()

            if operation == "Check balance":
                print(f"Your balance is {int(my_account_balance)}")
            elif operation == "Deposit":
                enter_deposit = int(input("How much do you want to enter deposit? "))               
                my_account_balance += enter_deposit
                print(f"Now your current balance is\t{my_account_balance}")
            elif operation == "Withdraw":
                withdraw_amount = int(input("How much do you want to Withdraw? "))
                my_account_balance -= withdraw_amount
                print(f"Now after Withdraw, your current balance is: {int(my_account_balance)}")
            elif operation == "Logout":
                print("Logout successful")
                break
            else:
                print("Invalid option")
                
            
            again = input("Do you want to perform again? Yes or No: ")
            if again == "No":
                condition = False
                print("Logout successful")

    except Exception as e:
        print(f"An error occurred: {e}")
