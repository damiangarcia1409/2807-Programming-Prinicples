

def containsDigits(s):
    hasDigit = False
    for letter in range(len(s)):
        if s[letter].isdigit():
            hasDigit = True

    if hasDigit:
        print("Has no digits: False")
    if not hasDigit:
        print("Has no digits: True")


while True:
    x = input("Enter a string: ")
    containsDigits(x)
