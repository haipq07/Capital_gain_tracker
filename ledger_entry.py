from linked_deque import LinkedDeque

class LedgerEntry:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.purchases = LinkedDeque()
# Add a new purchase to the entry
    def add_purchase(self, new_purchase):
        self.purchases.add_to_back(new_purchase)
 # Remove and return the oldest purchase from the entry
    def remove_purchase(self):
        return self.purchases.remove_front()

    def equals(self, other):# Check if this entry is equal to another based on stock symbol
        return self.stock_symbol == other.stock_symbol

    def display_entry(self):
        print(f"{self.stock_symbol}: ", end="")
        current = self.purchases.front
        while current is not None:
            print(f"{current.get_data().cost_per_share} ({current.get_data().shares} shares)", end=", ")
            current = current.get_next_node()
        print()
