partNumber = 4
ParticipantData = []
RegPart = 0
outPutFile = open("participantData.txt", "w")

while(RegPart < partNumber):
    TempartData =[]
    name = input("Enter Name: ")
    TempartData.append(name)
    country = input("Enter country: ")
    TempartData.append(country)
    Age = int(input("Enter Age: "))
    TempartData.append(Age)

    print(TempartData)
    ParticipantData.append(TempartData)
    print(ParticipantData)

    RegPart += 1

for participant in ParticipantData:
    for data in participant:
        outPutFile.write(str(data))
        outPutFile.write(" ")

    outPutFile.write("\n")

outPutFile.close()

inputFile = open("participantData.txt", "r")
inputList =[]

for line in inputFile:
    tempParticipant = line.strip("\n").split()
    #print(tempParticipant)
    inputList.append(tempParticipant)
    #print(inputList)

Age = {}
for part in inputList:
    tempAge = int(part[-1])
    if tempAge in Age:
        Age[tempAge] += 1
    else:
        Age[tempAge] = 1

print(Age)

Countries = {}
for count in inputList:
    tempCont = (count[-2])
    if tempCont in Countries:
        Countries[tempCont] += 1
    else:
        Countries[tempCont] = 1

print(Countries)
#Age statistics
Oldest = 0
youngest = 50
CommonAge = 0
Counter = 0
for age in Age:
    if age > Oldest:
        Oldest = age

    if age < youngest:
        youngest = age
    if  Age[age] > Counter:
        Counter = Age[age]
        CommonAge = age

print("The oldest age is:",Oldest)
print("The youngest age is:", youngest)
print("Most Occuring age is:",CommonAge, "with", Counter, "participants")
inputFile.close()