baseWage = 30.25
hourCap = 37
salesMinimum = 3000.00
sales = 0
hoursWorked = 0
overTimeHours = 0
pay = 0

hoursWorked = int(input("How many hours were worked?"))

if hoursWorked > 37:
    overTimeHours = hoursWorked - 37
    hoursWorked = hoursWorked - overTimeHours

pay = pay + (hoursWorked*30.25) + ((30.25*1.5)*overTimeHours)
#print(pay)


sales = int(input("Total sales for the week?"))
if sales > 3000:
    sales = sales - 3000
    sales = sales * 0.03
else:
    sales = 0

#print(sales)

print(sales + pay)



