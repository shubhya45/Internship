# text_utils.py

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    return sum(1 for char in sentence if char in vowels)

def count_consonants(sentence):
    vowels = "aeiouAEIOU"
    return sum(1 for char in sentence if char.isalpha() and char not in vowels)
