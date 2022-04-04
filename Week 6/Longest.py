# Workshop 5 Exercise 4

# 4.2

longest_string_count = 0
longest_string = ''
def longest_string_repeater():
    global longest_string_count
    global longest_string
    inputed_string = str(input('Enter a string: '))

    if inputed_string == '':
        print('Longest was:', longest_string)
    else:
        print (longest_string, longest_string_count)
        if len(inputed_string) > longest_string_count:
            longest_string = inputed_string
            longest_string_count = len(inputed_string)
            longest_string_repeater()
        else:
            longest_string_repeater()

# Execute function
longest_string_repeater()
