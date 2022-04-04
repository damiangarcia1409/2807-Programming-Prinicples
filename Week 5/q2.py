givenInt = input("Enter a number:")

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


answer = isqrt(float(givenInt))
print(answer)