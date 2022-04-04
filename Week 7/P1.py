file_name = str(input("File name: "))
lines = int(input("Lines: "))
file = open(file_name, "r")
content = file.read().split('\n')
count = 0

for x in content:
    if content.index(x) == lines:
        break
    else:
        print(x)
