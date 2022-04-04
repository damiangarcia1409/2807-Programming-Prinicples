# Workshop 5 Exercise 4

# 4.4
import re


has_digits = False

def no_digits():
    global has_digits

    string = input('Enter a string: ')

    if string != '':
        has_digits = bool((re.search(r'\d', string)))
        print('Has no digits:', str(has_digits))
        no_digits()

# exec function
no_digits()
