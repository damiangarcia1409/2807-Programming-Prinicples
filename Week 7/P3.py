def avg(numbers):
    val = (sum(numbers)/len(numbers))
    return round(val, 1)

def median(numbers):
    n = len(numbers)

    if n % 2 == 0:
        m_right = numbers[n//2]
        m_left = numbers[n//2 - 1]
        val = ((m_right + m_left)/2)
    else:
        val = numbers[n//2]
    return val

file_name = input("File name: ")
file = open(file_name, "r")
#content = file.readline()
content = file.read().split('\n')
content = sorted(content)
print(content)
numbers = [float(x) for x in content]
count = len(content)

print("Average =", avg(numbers))
print("Median =", median(numbers))