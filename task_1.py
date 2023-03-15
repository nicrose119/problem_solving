#Task 1 Reverse a String
# Write code that takes a string as input and returns the string reversed
# i.e. “Hello” will be returned as “olleH”

# 1. Write a function that takes in a string
# 2. Iterate over the string
# 3. Return the string in reverse

def string_reverser(text):
    reversed_string = ""
    for char in text:
        reversed_string = char + reversed_string
    print(reversed_string) 

string_reverser('Hello')
