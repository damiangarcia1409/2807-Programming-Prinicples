marks = int(input("How many marks? "))

if marks >= 90:
    print("gum leaf cluster")
elif marks < 90 and marks >= 60:
    print("leafy twig")
elif marks < 60 and marks >= 45:
    print("gum leaf")
else:
    print("dead twig")