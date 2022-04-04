coordinates = []
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# '^[A-Z][0-9][0-6]?$'
interval = 0.5

def pythagoras_theorem(a, b):
    return (a ** 2 + b ** 2)

def calc_trip(a, b):
    global coordinates
    interval = 0
    start = None

    for i in coordinates:
        if i == a:
            start = coordinates.index(i)

    for j in coordinates[start:]:
        interval = interval + 0.5
        if j == b:
            return interval

def validate_input(usr_input):
    global coordinates
    input_coords = []
    try:
        for i in usr_input:
            coord = (str(i[0]), int(i[1:]))

            if coord in coordinates:
                input_coords.append(coord)
            else:
                print("Bad reference:", i)
                exit()
        return input_coords
    except ValueError:
        print("Bad reference:", i)
        exit()

for i in range(26):
    for j in alphabet:
        coordinates.append((j, i + 1))

# MAIN PROGRAM
usr_inputs = input("Enter trip map references: ")
usr_coords = usr_inputs.split()
usr_map = validate_input(usr_coords)
intervals_1 = calc_trip(usr_map[0], usr_map[1])
intervals_2 = calc_trip(usr_map[1], usr_map[2])
total = pythagoras_theorem(intervals_1, intervals_2)
print("Total distance =", round((total/1000), 1), "km")




