file_name = input("File name: ")

lines = 0
words = 0
chars = 0

# To NOT store all lines in memory, we'll ad-hoc count
with open(file_name) as fn:
    for l in fn:
        lines = lines + 1
        words = words + len(l.split())
        chars = chars + len(l)

print("Characters:", chars)
print("Words", words)
print("lines", lines)
