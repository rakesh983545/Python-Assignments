#Task 2: Create Another Module (string_utils.py)
#Create a module string_utils.py with:
#1. capitalize_words(text) → returns text with each word capitalized
#2. reverse_string(text) → returns reversed string
#3. word_count(text) → returns number of words in the text
#Import this module in main.py and test all functions.
def capitalize_words(text):
    return text.title()

def reverse_string(text):
    return text[::-1]

def word_count(text):
    return len(text.split())