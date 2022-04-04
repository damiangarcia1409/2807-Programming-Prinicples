number = []

while True:
    num = input("Enter a number: ")
    if num == "":
        break
    else:
        number.append(num)
a = sorted(number)
b = (len(a) +1)/2

print("Median =", b)

