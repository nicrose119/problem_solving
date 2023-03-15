"""
Palindrome
1. Take user input
2. Check to see if it is a palindrome
    does the string read forward the same way it reads in reverse? 
3. Report Results
    print to console results
"""
from task_1 import string_reverser

def is_palindrome(string):
    if len(string)<1:
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:1])
    else:
        return False
        

user_string = input('Enter a word to see if it is a Palindrome: ')
print(user_string)

string_reverser(user_string)

if is_palindrome(user_string) == True:
    print(f'{user_string} is a palindrome')
else:
    print(f'{user_string} is NOT a palindrome')
