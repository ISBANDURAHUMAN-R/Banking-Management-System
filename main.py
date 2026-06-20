import csv
import os

ACCOUNTS_FILE = "accounts.csv"
TRANSACTIONS_FILE = "transactions.csv"


def create_files():
    if not os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Account No", "Name", "Balance"])

    if not os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Account No", "Type", "Amount"])


def create_account():
    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit: "))

    with open(ACCOUNTS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([acc_no, name, balance])

    print("Account Created Successfully!")


def find_account(acc_no):
    with open(ACCOUNTS_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == acc_no:
                return row

    return None


def update_balance(acc_no, new_balance):
    rows = []

    with open(ACCOUNTS_FILE, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        if row[0] == acc_no:
            row[2] = str(new_balance)

    with open(ACCOUNTS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def deposit():
    acc_no = input("Enter Account Number: ")

    account = find_account(acc_no)

    if account:
        amount = float(input("Enter Amount: "))
        balance = float(account[2]) + amount

        update_balance(acc_no, balance)

        with open(TRANSACTIONS_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([acc_no, "Deposit", amount])

        print("Deposit Successful!")
    else:
        print("Account Not Found!")


def withdraw():
    acc_no = input("Enter Account Number: ")

    account = find_account(acc_no)

    if account:
        amount = float(input("Enter Amount: "))
        balance = float(account[2])

        if amount <= balance:
            balance -= amount

            update_balance(acc_no, balance)

            with open(TRANSACTIONS_FILE, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([acc_no, "Withdraw", amount])

            print("Withdrawal Successful!")
        else:
            print("Insufficient Balance!")
    else:
        print("Account Not Found!")


def check_balance():
    acc_no = input("Enter Account Number: ")

    account = find_account(acc_no)

    if account:
        print("\nAccount Holder:", account[1])
        print("Balance: ₹", account[2])
    else:
        print("Account Not Found!")


def transaction_history():
    acc_no = input("Enter Account Number: ")

    print("\nTransaction History")

    with open(TRANSACTIONS_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == acc_no:
                print(row)


def main():
    create_files()

    while True:
        print("\n===== BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            check_balance()

        elif choice == "5":
            transaction_history()

        elif choice == "6":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()
