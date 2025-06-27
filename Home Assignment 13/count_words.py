# 🔹 **Part D: Understanding __name__ == "__main__"
# 9.	Create a file count_words.py:
# o	Defines a function count_words(sentence).
# o	If run directly (if __name__ == "__main__":), ask the user for a sentence and print the word count.
# o	Import this module in another script and use count_words().


def count_words(sentence):
    words = sentence.split()
    return len(words)

if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    print("Word count:", count_words(user_input))
