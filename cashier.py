class Cashier:

    def __init__(self):
        self.coins = [1, 5, 10, 25, 50]
    
    def calculate_change(self, amount_paid, item_price):
        raise NotImplementedError()
    
    def budget_options(self, budget, current_items):
        raise NotImplementedError()