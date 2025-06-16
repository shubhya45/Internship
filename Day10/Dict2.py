# Replace Words with Frequencies
# Input: "cat dog cat rat dog cat"
# Output: "3 2 3 1 2 3"
# dict2="cat dog cat rat dog cat"

string4 = "cat dog cat rat dog cat"
words=string4.split()
print(words)
list=[str(words.count(word)) for word in words]
str=" ".join(list)
print(str)
c_count=string4.count("cat")
c_count=string4.count("dog")
c_count=string4.count("rat")