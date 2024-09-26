class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print('Please insert coins.')
        dollars = int(input('How many dollars?: '))
        half_dollars = int(input('How many half dollars?: '))
        quarters = int(input('How many quarters?: '))
        nickels = int(input('How many nickels?: '))
        return dollars + half_dollars * 0.5 + quarters * 0.25 + nickels * 0.05

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        return coins >= cost