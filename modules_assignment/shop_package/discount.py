#discount.py
#Functions:
#1. apply_discount(price, percent) → returns discounted price
#2. flat_discount(price) → always subtracts 50 from price
def apply_discount(price, percent):
    discount_amount = price * (percent / 100)
    return price - discount_amount

def flat_discount(price):
    return price - 50
    