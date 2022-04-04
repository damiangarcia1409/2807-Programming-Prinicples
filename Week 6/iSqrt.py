# Workshop 5 Exercise 4

# 4.3

value = 0
num = float(input('Enter a number: '))
a = num
x = (a + 1) // 2
while x < a:
    a = x
    x = (a + num // a) // 2
    value = x
print('Integer square root =', str(int(value)))
