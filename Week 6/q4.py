strings = input("Enter a string: ")

def reverse_string(string):
    return string[::-1]

count = 0

reversed_strings = reverse_string(strings)

for x, y in zip(strings, reversed_strings):
    if x.lower() is y.lower():
        print("It is not a palindrone")
        count = 1
        break

if count == 0:
    print("It is a palindrone!")

