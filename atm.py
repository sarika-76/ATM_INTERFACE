class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

class ATM:
    def __init__(self):
        self.users = {}  # Store users in a dictionary with user_id as keys

    def add_user(self, user):
        self.users[user.user_id] = user

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        return None

    def deposit(self, user, amount):
        user.balance += amount
        user.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, user, amount):
        if user.balance >= amount:
            user.balance -= amount
            user.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds.")

    def transfer(self, sender, receiver, amount):
        if sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
            sender.transaction_history.append(f"Transferred ${amount} to {receiver.user_id}")
            receiver.transaction_history.append(f"Received ${amount} from {sender.user_id}")
        else:
            print("Insufficient funds.")

    def transaction_history(self, user):
        for transaction in user.transaction_history:
            print(transaction)

def main():
    atm = ATM()

    while True:
        print("\nATM Menu:")
        print("1. Create User")
        print("2. Login")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter a user ID: ")
            pin = input("Enter a PIN: ")
            user = User(user_id,pin)
            atm.add_user(user)
            print("User created successfully.")

        elif choice == "2":
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")

            user = atm.authenticate_user(user_id, pin)
            if user:
                while True:
                    print("\nUser Menu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. Transaction History")
                    print("5. Logout")

                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        amount = float(input("Enter the amount to deposit: "))
                        atm.deposit(user, amount)
                    elif user_choice == "2":
                        amount = float(input("Enter the amount to withdraw: "))
                        atm.withdraw(user, amount)
                    elif user_choice == "3":
                        receiver_id = input("Enter the receiver's user ID: ")
                        receiver = atm.users.get(receiver_id)
                        if receiver:
                            amount = float(input("Enter the amount to transfer: "))
                            atm.transfer(user, receiver, amount)
                        else:
                            print("Receiver not found.")
                    elif user_choice == "4":
                        atm.transaction_history(user)
                    elif user_choice == "5":
                        print("Logout successful.")
                        break
                    else:
                        print("Invalid choice. Try again.")
            else:
                print("Authentication failed. Please try again.")

        elif choice == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Try again.")

if __name__== "__main__":
    main()