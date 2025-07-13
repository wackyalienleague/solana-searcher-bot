# models/bundle.py

class Bundle:
    def __init__(self, transactions, tip, strategy="generic"):
        self.transactions = transactions
        self.tip = tip
        self.strategy = strategy
