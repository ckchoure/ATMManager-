from plyer import notification

pass_book = {
    "name" : "Chain kumar choure",
    "account_number" : 123456789,
    "ifsc_coe" : "SBI000123",
    "branch_code" : 1567,
    "mobile_number" : 9301938638,
    "dob" : "03/03/2003",
    "address" : "Chhindwara",
    "email" : "chainkumarchoure49@gmail.com",
    "pin" : 1234,
    "balance" : 5000
}

# Login system with PIN verification and account lock
attempts = 3
while attempts > 0:
    user_pin = int(input("Enter your PIN: "))

    if pass_book["pin"] == user_pin:
        print("\nLogin successful!")
        # ATM Menu
        while True:
            print("\n\tATM Menu")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Change PIN")
            print("5. View Account History")
            print("6. Quit")

            choice = int(input("\nPlease Enter your choice: "))

            # Check user choice
            if choice == 1:
                print(f"Your current balance is: {pass_book['balance']}")

            # Withdraw money    
            elif choice == 2:
                amount = int(input("Enter Amount to Withdraw: "))
                if amount <= pass_book["balance"]:
                    pass_book["balance"] -= amount
                    print("\nWithdrawal successful.")
                    print(f"Your available balance is: {pass_book['balance']}")

                    # for notification
                    notification.notify(
                        title = "Bank Update",
                        message = f"Rs.{amount} is Withdraw to A/C xxx789. Avl Bal: Rs. {pass_book['balance']}",
                        app_icon = "avalanche_crypto_coin_icon_256894.ico",
                        timeout = 10,
                    )  # type: ignore

                else:
                    print("Insufficient funds!")

            # Deposit money
            elif choice == 3:
                amount = int(input("Enter Amount to Deposit: "))
                pass_book["balance"] += amount
                print("\nDeposit successful.")
                print(f"Your available balance is: {pass_book['balance']}")

                # for notification
                notification.notify(
                    title = "Bank Update",
                    message = f"Rs.{amount} is Deposit to A/C xxx789. Avl Bal: Rs. {pass_book['balance']}",
                    app_icon = "avalanche_crypto_coin_icon_256894.ico",
                    timeout = 10,
                    )  # type: ignore

            # Change PIN
            elif choice == 4:
                old_pin = int(input("Enter your old PIN: "))

                if pass_book["pin"] == old_pin:
                    new_pin = int(input("Enter your new PIN: "))
                    pass_book.update({"pin": new_pin})
                    
                    # for notification
                    notification.notify(
                        title = "Bank Update",
                        message = f"Your A/C xxx789 PIN successfully updated. PIN is {new_pin}. Please don't shear this PIN.",
                        app_icon = "avalanche_crypto_coin_icon_256894.ico",
                        timeout = 10,
                    ) # type: ignore
                else:
                    print("Incorrect old PIN")

            # Account History
            elif choice == 5:
                print("\nAccount Details:")
                for key, value in pass_book.items():
                    print(f"{key.capitalize()}: {value}")

            # Quit
            elif choice == 6:
                print("\nThank you for using the ATM. Goodbye!")
                break

            # Invalid Choice
            else:
                print("\nInvalid choice. Please choose a number between 1 and 6.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect PIN. You have {attempts} attempts left.")
        else:
            print("Your account has been locked due to multiple incorrect PIN attempts.")
            print("To unlock, contact our helpline at 1800-123-4567 or visit the nearest branch.")

            # for notification
            notification.notify(
                        title = "Security Update",
                        message = "Your A/C xxx789 has been locked due to multiple incorrect PIN attempts. Try again after 24 hours or contact customer support.",
                        app_icon = "avalanche_crypto_coin_icon_256894.ico",
                        timeout = 10,
                    ) # type: ignore