
import math

def carpetCalulator(x,y):
    width = 0.0
    length = 0.0

    carpetRollWidth = 3.66

    if x > y:
        length = x
        width = y
    else:
        width = x
        length = y

    print("Length = "+str(length)+" m")
    print("Width = "+str(width)+" m")

    lengthwayrolls = math.ceil(width / carpetRollWidth)
    lengthwayrolls = math.ceil(lengthwayrolls * length)

    print("lenght required length ways:" + str(lengthwayrolls))

    widthwayrolls = math.ceil(length/carpetRollWidth)
    widthwayrolls = math.ceil(widthwayrolls * width)
    print("lenght required width ways:" + str(widthwayrolls))

while True:
    d1 = float(input("Enter dimension 1: "))
    d2 = float(input("Enter dimension 2: "))
    carpetCalulator(d1,d2)