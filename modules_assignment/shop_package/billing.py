#billing.py
#Functions:
#1. calculate_total(prices) → returns total bill (sum of all prices)
#2. apply_tax(amount) → adds 5% tax
def calculate_total(prices):
    return sum(prices)

def apply_tax(amount):
    return amount * 1.05   
    