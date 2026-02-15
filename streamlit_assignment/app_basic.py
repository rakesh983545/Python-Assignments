#Task 1: Basic Streamlit App (app_basic.py)
#Create a basic Streamlit app that:
#1. Displays a title: "Welcome to Streamlit!"
#2. Shows a text input box for entering your name.
#3. When user clicks a button "Greet Me", display:
#"Hello, !"
#Use:
#st.title()
#st.text_input()
#st.button()
#st. write()
import streamlit as st
# Set the title of the app
st.title("Welcome to Streamlit!")
# Create a text input box for entering the user's name
name = st.text_input("Enter your name:")
# Create a button that, when clicked, will greet the user
if st.button("Greet Me"):
    if name:  # Check if the user has entered a name
        st.write(f"Hello, {name}!")
    else:
        st.write("Please enter your name to be greeted.")
        