class User:
    def __init__(self, name, acc_no, pin, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def add_transaction(self, description):
        self.transactions.append(description)


def check_balance(user):
    print(f"\nYour current balance is: ₹{user.balance}")


def deposit(user):
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("Enter a valid amount.")
            return
        user.balance += amount
        user.add_transaction(f"Deposited ₹{amount}")
        print("Deposit successful.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def withdraw(user):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Enter a valid amount.")
            return
        if amount <= user.balance:
            user.balance -= amount
            user.add_transaction(f"Withdrew ₹{amount}")
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def transfer(user, users):
    acc_no = input("Enter recipient account number: ")
    recipient = None
    for u in users:
        if u.acc_no == acc_no and u != user:
            recipient = u
            break

    if recipient:
        try:
            amount = float(input("Enter amount to transfer: ₹"))
            if amount <= 0:
                print("Enter a valid amount.")
                return
            if amount <= user.balance:
                user.balance -= amount
                recipient.balance += amount
                user.add_transaction(f"Transferred ₹{amount} to {recipient.name}")
                recipient.add_transaction(f"Received ₹{amount} from {user.name}")
                print("Transfer successful.")
            else:
                print("Insufficient balance.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Recipient account not found.")


def show_transactions(user):
    print("\nTransaction History:")
    if not user.transactions:
        print("No transactions yet.")
    else:
        for t in user.transactions:
            print("-", t)


def authenticate(users):
    acc_no = input("Enter account number: ")
    pin = input("Enter PIN: ")
    for user in users:
        if user.acc_no == acc_no and user.pin == pin:
            return user
    return None


def atm_interface(users):
    print("\n==== Welcome to ATM ====")
    user = authenticate(users)
    if user:
        print(f"\nHello, {user.name}!")
        while True:
            print("\nChoose an option:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transfer Money")
            print("5. View Transaction History")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                check_balance(user)
            elif choice == '2':
                deposit(user)
            elif choice == '3':
                withdraw(user)
            elif choice == '4':
                transfer(user, users)
            elif choice == '5':
                show_transactions(user)
            elif choice == '6':
                print("Thank you for using ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
    else:
        print("Authentication failed. Invalid account number or PIN.")


if __name__ == "__main__":
    # Sample users
    users = [
        User("Swapna", "123456", "1111", 5000),
        User("Ravi", "654321", "2222", 3000)
    ]

    atm_interface(users)
