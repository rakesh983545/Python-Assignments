#Task 3: Product Form (app_product_form.py)
#Create a simple form Ul:
#1. Use Streamlit sidebar to enter:
#o Product Name
#• Category (selectbox with 3-5 options)
#• Price
#2. When user clicks "Add Product", show:
#• A success message
#• The product details in a clean format
#Use components:
#st.sidebar.text_input
#st.sidebar.selectbox
#st. sidebar.number_input
#st.sidebar.button
import streamlit as st
def main():
    st.title("Product Form")

    # Sidebar inputs
    product_name = st.sidebar.text_input("Product Name")
    category = st.sidebar.selectbox("Category", ["Electronics", "Clothing", "Books", "Home & Kitchen", "Sports"])
    price = st.sidebar.number_input("Price", min_value=0.0, step=0.01)

    # Add Product button
    if st.sidebar.button("Add Product"):
        if product_name and price > 0:
            st.success("Product added successfully!")
            st.write(f"**Product Name:** {product_name}")
            st.write(f"**Category:** {category}")
            st.write(f"**Price:** ${price:.2f}")
        else:
            st.error("Please enter a valid product name and price.")
if __name__ == "__main__":    main()
