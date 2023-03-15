"""
Compress A String of Characters
1. Take in a string of characters
2. Iterate over characters of the string
    for loop to iterate over each char and count each instance
3. Return a new string with the count of each character
"""

compressed_string = ''
string = 'AAAbbbCCCddd'
count = 1

for i in range(len(string)-1):
    if string[i] == string[i + 1]:
        count = count + 1
    else:
        compressed_string = compressed_string + string[i] + str(count)
        count = 1

compressed_string = compressed_string + string[i + 1] + str(count)
print(compressed_string)

