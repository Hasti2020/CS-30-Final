import random
quiz = open("house.txt", "r")
line = quiz.readline()
sorting = line.split(",")
# Color codes using ANSI escape sequences
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
ENDC = "\033[0m"  # Reset to default

house_list = []

while sorting[0] != "End":
    print(sorting[0])
    print("1. " + str(sorting[1]))
    print("2. " + str(sorting[2]))
    answer = input("Answer (1 or 2?): ")
    print("")
    if answer == "1":
        house_list.append(sorting[3])
        line = quiz.readline()
        sorting = line.split(",")
    elif answer == "2":
        house_list.append(sorting[4])
        line = quiz.readline()
        sorting = line.split(",")
    else:
        answer = input("Try again (enter)")
    
print(house_list)
g = house_list.count(" G")    
s = house_list.count(" S")
h = house_list.count(" H")
r = house_list.count(" R")

if g == 3:
    print(RED + "You are in...GRYFINDOR" + ENDC)
if s == 3:
    print(GREEN + "You are in...SLYTHERIN" + ENDC)
if r == 3:
    print(BLUE + "You are in...RAVENCLAW" + ENDC)
if h == 3:
    print(YELLOW + "You are in...HUFFLEPUFF" + ENDC)

    
        


