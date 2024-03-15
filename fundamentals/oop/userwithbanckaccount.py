class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)

# Example usage:
user1 = User("John Doe", "john@example.com")
print(f"Initial balance for {user1.name}:")
user1.account.display_account_info()  # Display initial balance

user1.make_deposit(1000)  # Make a deposit of $1000
print(f"Balance after deposit for {user1.name}:")
user1.account.display_account_info()  # Display updated balance

