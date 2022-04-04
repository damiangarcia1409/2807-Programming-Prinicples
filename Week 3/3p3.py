#import math
teamSize = 15
busCap = 38
bus2Hire = 0
noTeams = 0


noTeams = int(input("How many teams?"))
teamSize = teamSize * noTeams
teamSize = teamSize / busCap
rounded_up_x = int(-(-teamSize //1))

print(rounded_up_x)

#print(math.ceil(teamSize))
