from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""
    
    def __init__(self, name, balance):
        """Initialize an Account object."""
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= 0.00.')
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money to the account."""
        if amount < Decimal('0.00'):
            raise ValueError('Deposit amount must be positive.')
        self.balance += amount
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.balance:
            raise ValueError('Withdrawal amount must be <= to balance.')
        elif amount < Decimal('0.00'):
            raise ValueError('Withdrawal amount must be positive.')
        self.balance -= amount

# Test-driving the Account class
if __name__ == "__main__":
    # Create an Account object with a name and an initial balance
    account1 = Account('John Green', Decimal('50.00'))
    
    # Display the account name and balance
    print(f"Account Name: {account1.name}")
    print(f"Account Balance: {account1.balance}")
    
    # Deposit an amount into the account
    account1.deposit(Decimal('25.53'))
    print(f"Account Balance after deposit: {account1.balance}")
    
    # Attempt to withdraw a valid amount
    account1.withdraw(Decimal('20.00'))
    print(f"Account Balance after withdrawal: {account1.balance}")
    
    # Attempt to withdraw an amount greater than the balance (should raise ValueError)
    try:
        account1.withdraw(Decimal('100.00'))
    except ValueError as e:
        print(f"Error: {e}")
    
    # Attempt to deposit a negative amount (should raise ValueError)
    try:
        account1.deposit(Decimal('-123.45'))
    except ValueError as e:
        print(f"Error: {e}")
    
    # Attempt to withdraw a negative amount (should raise ValueError)
    try:
        account1.withdraw(Decimal('-10.00'))
    except ValueError as e:
        print(f"Error: {e}")
