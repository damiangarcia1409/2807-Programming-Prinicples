strings = []

is_over = False

while True:
    phrase = input("Enter a string: ")
    if phrase == '':
        break
    else:
        strings.append(phrase)

for word in sorted(strings):
    print(word)