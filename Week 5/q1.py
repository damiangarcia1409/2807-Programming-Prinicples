longestString = ""


tempString = ""


emptyString = False

while not emptyString:
    tempString = input("Enter a string:")
    if tempString == '':
        print("Longest was:'"+longestString+"'")
        emptyString = True

    if len(tempString) > len(longestString):
        longestString = tempString