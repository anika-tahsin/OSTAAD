class Banking:
    # Default User/Holder Name & Initial Balance:
    # * Set up a default User/Holder name and an initial 
    # balance for demonstration purposes.
    def __init__(self, username, initial_balance):
        self.name = username
        self.balance = initial_balance

    """Deposit Functionality:
    * Ensure that the deposit amount is greater than 0. 
    Negative values are not allowed."""

    def deposit(self, amount):
        if amount>0 :
            self.balance += amount
        return amount
    
    def get_balance(self):
        return self.balance

    """ Withdrawal Functionality:
    * Ensure the withdrawal amount does not exceed the 
    available balance.
    """

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return f"Insufficient Balance"

    """ Balance Inquiry:
    * Display the updated balance after every successful 
    deposit or withdrawal transaction."""

    


bank = Banking("Anika", 10000)
print(f"Account Name: {bank.name}")
print(f"Initial Balance: {bank.balance}")
print(f"Deposit Balance: {bank.deposit(1000)}")
print(f"After Deposit your balance is: {bank.get_balance()}")
print(f"Withdrawed Balance: {bank.withdraw(11000)}")
print(f"After withdraw your balance is: {bank.get_balance()}")