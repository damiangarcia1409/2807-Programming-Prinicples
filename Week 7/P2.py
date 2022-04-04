file_name = str(input("File name: "))
lines = int(input("Lines: "))
file = open(file_name, "r")
content = file.read().split('\n')
count = len(content)

if lines > count:
    for x in content:
        print(x)
else:
    for x in range(count - lines, count):
        print(content[x])

