#Task 2: Price Calculator (app_discount.py)
#Build a simple price calculator app that:
#1. Takes product price (number input)
#2. Takes discount percentage (slider from 0 to 50%)
#3. On button click, calculates discounted price
#4. Shows result using st.success()
#Example:
#Original Price: 1000
#Discount: 10%
#Final Price: 900
import streamlit as st
def calculate_discounted_price(price, discount):
    discounted_price = price * (1 - discount / 100)
    return discounted_price
def main():
    st.title("Price Calculator with Discount")
    price = st.number_input("Enter the product price:", min_value=0.0, step=0.01)
    discount = st.slider("Select discount percentage:", min_value=0, max_value=50, value=0)
    if st.button("Calculate Discounted Price"):
        final_price = calculate_discounted_price(price, discount)
        st.success(f"Final Price after {discount}% discount: ${final_price:.2f}")
if __name__ == "__main__":    main()
