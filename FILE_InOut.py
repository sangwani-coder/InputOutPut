vacationSpots = ["London","Paris", "Dubai", "Utah", "New York"]
vacationFile = open("vacationPlaces", 'w')

for spots in vacationSpots:
    vacationFile.write(spots + "\n")

vacationFile.close()

vacationFile = open("vacationPlaces", 'r')

for line in vacationFile:
    print(line, end="")

# wholeFile = vacationFile.read()
# print(wholeFile)
vacationFile.close()

with open("vacationPlaces", "r") as vacationFile:
    for line in vacationFile:
        print(line, end = "")
