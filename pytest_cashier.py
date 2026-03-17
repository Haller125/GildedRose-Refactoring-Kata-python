import pytest
from cashier import Cashier
from gilded_rose import Item


class TestCalculateChange:
    
    def test_calculate_change_exact_amount(self):
        cashier = Cashier()
        change = cashier.calculate_change(amount_paid=10, item_price=10)
        assert change == 0
    
    def test_calculate_change_overpaid(self):
        cashier = Cashier()
        change = cashier.calculate_change(amount_paid=20, item_price=7)
        assert change == 13
    
    def test_calculate_change_one_coin(self):
        cashier = Cashier()
        change = cashier.calculate_change(amount_paid=15, item_price=10)
        assert change == 5


class TestBudgetOptionsMaxTwoItems:
    
    def test_budget_options_two_item_combinations(self):
        cashier = Cashier()
        items = [
            Item("apple", 10, 5),
            Item("banana", 10, 5),
            Item("orange", 10, 5),
        ]
        budget = 10
        combinations = cashier.budget_options(budget, items)
        
        assert len(combinations) == 3
        assert all(isinstance(combo, (list, tuple)) for combo in combinations)
        for combo in combinations:
            total = sum(item.price for item in combo)
            assert total == budget


class TestBudgetOptionsMaxThreeItems:
    
    def test_budget_options_three_item_combinations(self):
        cashier = Cashier()
        items = [
            Item("item_1", 10, 3),
            Item("item_2", 10, 3),
            Item("item_3", 10, 3),
            Item("item_4", 10, 3),
        ]
        budget = 9
        combinations = cashier.budget_options(budget, items)
        
        assert len(combinations) > 0
        for combo in combinations:
            assert len(combo) == 3
            total = sum(item.price for item in combo)
            assert total == budget


class TestBudgetOptionsMaxFourItems:
    
    def test_budget_options_four_item_combinations(self):
        cashier = Cashier()
        items = [
            Item("item_1", 10, 2),
            Item("item_2", 10, 2),
            Item("item_3", 10, 2),
            Item("item_4", 10, 2),
            Item("item_5", 10, 2),
        ]
        budget = 8
        combinations = cashier.budget_options(budget, items)
        
        assert len(combinations) > 0
        for combo in combinations:
            assert len(combo) == 4
            total = sum(item.price for item in combo)
            assert total == budget


class TestBudgetOptionsMaxFiveOrMoreItems:
    
    def test_budget_options_five_plus_item_combinations(self):
        cashier = Cashier()
        items = [
            Item("item_1", 10, 1),
            Item("item_2", 10, 1),
            Item("item_3", 10, 1),
            Item("item_4", 10, 1),
            Item("item_5", 10, 1),
            Item("item_6", 10, 1),
        ]
        budget = 6
        combinations = cashier.budget_options(budget, items)
        
        assert len(combinations) > 0
        for combo in combinations:
            assert len(combo) >= 5
            total = sum(item.price for item in combo)
            assert total == budget
