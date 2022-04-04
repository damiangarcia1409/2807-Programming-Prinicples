# Workshop 5 Exercise 4

# 4.5

rolls = 3.66

dim1 = float(input('Enter room dimension 1 (m): '))
dim2 = float(input('Enter room dimension 2 (m): '))

if dim1 > dim2:
    length = dim1
    width = dim2
else:
    length = dim2
    width = dim1

print('Length =', (length))
print('Width =', width)

print('Total length required lengthways =', length_ways, 'm')
print('Total length required widthways =', width_ways, 'm')
