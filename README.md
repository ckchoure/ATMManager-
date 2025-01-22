# ATM Manager

## Overview
ATM Manager is a Python-based project that simulates an ATM system with features such as PIN verification, account balance management, money withdrawal and deposit, PIN change, and transaction notifications. It ensures security by locking the account after multiple incorrect PIN attempts.

## Features
- **Login System**: PIN-based authentication with a maximum of 3 attempts before account lock.
- **Account Management**:
  - Check account balance.
  - Withdraw money with sufficient funds.
  - Deposit money into the account.
  - Change the PIN securely.
- **Transaction Notifications**: Real-time notifications for withdrawals, deposits, and PIN changes using the Plyer library.
- **Account History**: View account details securely.
- **Security**: Automatic account lock after 3 incorrect PIN attempts, with a recovery process.

## Technology Stack
- **Programming Language**: Python
- **Libraries Used**:
- "Plyer" for desktop notifications.

  ## How It Works
1. Run the script and enter your PIN to log in.
2. After successful login, choose an option from the ATM menu:
   - **Check Balance**: Displays your current account balance.
   - **Withdraw Money**: Deducts the entered amount from your balance (if sufficient funds are available).
   - **Deposit Money**: Adds the entered amount to your account balance.
   - **Change PIN**: Updates your account PIN after verifying the old PIN.
   - **View Account History**: Shows all account details securely.
   - **Quit**: Exits the ATM system.
3. Real-time notifications:
   - Receive desktop notifications for withdrawals, deposits, and PIN changes.
4. Security Features:
   - You have 3 attempts to enter the correct PIN.
   - After 3 incorrect attempts, the account is locked, and recovery instructions are displayed.


