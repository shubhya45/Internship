# Create a Book Class

# Attributes:

# title, author, year.

# Method:

# get_description() — Returns a formatted description like:

# "The book 'Title' by Author was published in Year."

# Test it: Create a book and print its description.

class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def get_description(self):
        print(f"The book {self.title} by {self.author} was published in {self.year}")
b1=Book("Trignometry","hjhhvj",2001)
b1.get_description()        
    