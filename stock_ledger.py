from ledger_entry import LedgerEntry
from stock_purchase import StockPurchase

class StockLedger:
    def __init__(self):
        self.entries = []#create empty list for stock entries

    def buy(self, stock_symbol, shares_bought, price_per_share): #check if that symbol already in entries
        for entry in self.entries:
            if entry.equals(LedgerEntry(stock_symbol)):
                entry.add_purchase(StockPurchase(stock_symbol, price_per_share, shares_bought))
                return# if not, create new stock ledgerentry for that symbols
        new_entry = LedgerEntry(stock_symbol)
        new_entry.add_purchase(StockPurchase(stock_symbol, price_per_share, shares_bought))
        self.entries.append(new_entry) # add into list

    def sell(self, stock_symbol, shares_sold, price_per_share):
        for entry in self.entries:
            if entry.equals(LedgerEntry(stock_symbol)):
                total_cost = 0
                shares_remaining = shares_sold

                while shares_remaining > 0 and not entry.purchases.is_empty():
                    purchase = entry.remove_purchase()
                    if purchase.shares > shares_remaining:
                        total_cost += purchase.cost_per_share * shares_remaining
                        purchase.shares -= shares_remaining# Update remaining shares
                        entry.add_purchase(purchase) # Return the remaining shares to the entry
                        shares_remaining = 0
                    else:
                        total_cost += purchase.cost_per_share * purchase.shares
                        shares_remaining -= purchase.shares

                gain_loss = (price_per_share * (shares_sold - shares_remaining)) - total_cost
                print(f"Sold {shares_sold} shares of {stock_symbol} for a total gain/loss of ${gain_loss:.2f}")
                return

    def display_ledger(self):
        print("---- Stock Ledger ----")
        for entry in self.entries:
            entry.display_entry()
