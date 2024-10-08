from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance with controlled access."""

    def __init__(self, name, balance):
        """Initialize an Account object."""
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= 0.00.')
        self._name = name         # Leading underscore indicates internal use
        self._balance = balance   # Leading underscore indicates internal use

    @property
    def name(self):
        """Return the account name."""
        return self._name

    @property
    def balance(self):
        """Return the account balance."""
        return self._balance

    @balance.setter
    def balance(self, amount):
        """Set the account balance with validation."""
        if amount < Decimal('0.00'):
            raise ValueError('Balance must be >= 0.00.')
        self._balance = amount

    def deposit(self, amount):
        """Deposit money to the account."""
        if amount < Decimal('0.00'):
            raise ValueError('Deposit amount must be positive.')
        self._balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self._balance:
            raise ValueError('Withdrawal amount must be <= to balance.')
        elif amount < Decimal('0.00'):
            raise ValueError('Withdrawal amount must be positive.')
        self._balance -= amount

# Test-Driving the Updated Account Class
if __name__ == "__main__":
    # Create an Account object
    account1 = Account('John Green', Decimal('50.00'))

    # Access the name and balance using getter methods
    print(f"Account Name: {account1.name}")
    print(f"Account Balance: {account1.balance}")

    # Set a new valid balance using the setter method
    account1.balance = Decimal('100.00')
    print(f"Account Balance after setting: {account1.balance}")

    # Attempt to set an invalid (negative) balance (should raise ValueError)
    try:
        account1.balance = Decimal('-1000.00')
    except ValueError as e:
        print(f"Error: {e}")

    # Deposit money into the account
    account1.deposit(Decimal('50.00'))
    print(f"Account Balance after deposit: {account1.balance}")

    # Withdraw money from the account
    account1.withdraw(Decimal('20.00'))
    print(f"Account Balance after withdrawal: {account1.balance}")
