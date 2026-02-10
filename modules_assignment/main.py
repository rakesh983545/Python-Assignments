import math_utils
from math_utils import square
import string_utils
# Testing the functions from math_utils
a = 10
b = 5
print(f"Addition of {a} and {b}: {math_utils.add(a, b)}")
print(f"Subtraction of {b} from {a}: {math_utils.subtract(a, b)}")
n = 4
print(f"Square of {n}: {square(n)}")
# Testing the functions from string_utils
text = "hello world"
print(f"Capitalized Words: {string_utils.capitalize_words(text)}")
print(f"Reversed String: {string_utils.reverse_string(text)}")
print(f"Word Count: {string_utils.word_count(text)}")

#add:
#from discount import apply_discount, flat _discount
#from billing import calculate_total, apply_tax
#(This allows calling functions directly from the package)
from shop_package.discount import apply_discount, flat_discount
from shop_package.billing import calculate_total, apply_tax
prices = [100, 200, 300]
print(calculate_total(prices))
total = calculate_total(prices)
print(apply_tax(total))
price = 1000
discounted_price = apply_discount(price, 10)
print(f"Price after 10% discount: {discounted_price}")
flat_discounted_price = flat_discount(price)
print(f"Price after flat discount: {flat_discounted_price}")



