# 🔹 Part F: Real-World Practice
# 13.	Create a string_utils.py:
# o	count_characters(s) → returns character count.
# o	count_words(s) → returns word count.
# o	reverse_string(s) → returns the reversed version.
# o	Import and test these in main.py.

def count_characters(s):
    print("Character count: ", len(s))
    
def count_words(s):
    words = s.split()
    print("Word count: ", len(words))   

def reverse_string(s):
    reversed_s = s[::-1]
    print("Reversed string: ", reversed_s)
    
    