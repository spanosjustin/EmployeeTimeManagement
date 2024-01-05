# Clock in and track work hours
from datetime import datetime
import sys

# Initializing Data
running = True

# Get and format the currewnt date and time
now = datetime.now()
dateAndTime = now.strftime("%d/%m/%y %H:%M")
shiftHour = 0
shiftMinute = 0
totalShift = 0
weeklyHoursWorked = 0.00

# Intitializing Data Base
employeeData = {
    123456: {
        "name": "Justin Spanos",
        "isClockedIn": False,
        "Hourly Rate": 17.75
        },
    654321: {
        "name": "Natalia Spanos",
        "isClockedIn": False,
        "Hourly Rate": 18.00
        },
    111111: {
        "name": "Yo Momma",
        "isClockedIn": False,
        "Hourly Rate": 15.70
        }
    }

# For Later
employeeWorkWeekData = {
    123456: {
        "in":{},
        "out":{},
        "shifts":{},
        "total hours":{},
        },
    654321: {
        "in":{},
        "out":{},
        "shifts":{},
        "total hours":{},
        },
    111111: {
        "in":{},
        "out":{},
        "shifts":{},
        "total hours":{},
        }
    }

# Functions
# loads data from a .txt file
##try:
##    with open("employeeWorkWeekData.txt", "r") as file:
##        employeeData = str(file.read())
##except FileNotFoundError:
##    print("No data")
##
### save function
##def saveData():
##    with open("employeeWorkWeekData.txt", "w") as file:
##        file.write(str(employeeWorkWeekData))

# Prints invalid inputs
def invalidFunction():
    print("Invalid Number")

def clockIn():
    global employeeInUse
    global employeeData
    global employeeWorkWeekData
    currentTime = datetime.now()
    timeIn = currentTime.strftime("%d/%m/%y %H:%M")
    if employeeInUse in employeeData:
        employeeData[employeeInUse]["isClockedIn"] = True
        print()
        print("==================================")
        print("           Clocked In")
        print("        ", employeeData[employeeInUse]["name"])
        print("   Clocked in at:", dateAndTime)
        print("==================================")
        print()
        for x in range(len(employeeWorkWeekData[employeeInUse]["in"]) + 1):
            if(x >= len(employeeWorkWeekData[employeeInUse]["in"])):
                employeeWorkWeekData[employeeInUse]["in"][x] = timeIn

def clockOut():
    global employeeInUse
    global employeeData
    global employeeWorkWeekData
    currentTime = datetime.now()
    timeIn = currentTime.strftime("%d/%m/%y %H:%M")
    if employeeInUse in employeeData:
        employeeData[employeeInUse]["isClockedIn"] = False
        recentShift = len(employeeWorkWeekData[employeeInUse]["shifts"])
        print()
        print("==================================")
        print("           Clocked Out")
        print("        ", employeeData[employeeInUse]["name"])
        print("   Clocked out at:", dateAndTime)
        print("==================================")
        print()
        for x in range(len(employeeWorkWeekData[employeeInUse]["out"]) + 1):
            if(x >= len(employeeWorkWeekData[employeeInUse]["out"])):
                employeeWorkWeekData[employeeInUse]["out"][x] = timeIn

def shiftLength():
    global employeeInUse
    global employeeWorkWeekData
    global shiftMinute
    global shiftHour
    # Variables
    clockInTime = str(employeeWorkWeekData[employeeInUse]["in"])
    clockOutTime = str(employeeWorkWeekData[employeeInUse]["out"])
    
    clockInHour = int(clockInTime[14:16])
    clockInMin = int(clockInTime[17:19])
    clockOutHour = int(clockOutTime[14:16])
    clockOutMin = int(clockOutTime[17:19])
    
    # Logic for hours
    if(clockOutHour >= clockInHour):
        shiftHour = clockOutHour - clockInHour
    else:
        clockOutHour += 24
        shiftHour = clockOutHour - clockInHour
    # Logic for minutes
    if(clockOutMin >= clockInMin):
        shiftMinute = clockOutMin - clockInMin
    else:
        clockOutMin += 60
        shiftMinute = clockOutMin - clockInMin
    # Combine Minutes and hours
    shiftMinute = round((shiftMinute / 60), 2)
    totalShift = shiftHour + shiftMinute
    for x in range(len(employeeWorkWeekData[employeeInUse]["shifts"]) + 1):
        if(x >= len(employeeWorkWeekData[employeeInUse]["shifts"])):
            employeeWorkWeekData[employeeInUse]["shifts"][x] = totalShift
            employeeWorkWeekData[employeeInUse]["shifts"][x]
    print(employeeWorkWeekData[employeeInUse]["shifts"][len(employeeWorkWeekData[employeeInUse]["shifts"])-1])

# add up and calculate the total hours of the week
def totalWeeklyHours():
    global employeeInUse
    global employeeWorkWeekData
    global weeklyHoursWorked
    print()
    employeeCalc = int(input("Enter Employee Numbers: "))
    print()
    for x in range(len(employeeWorkWeekData[employeeCalc]["shifts"]) + 1):
        #if(x >= len(employeeWorkWeekData[employeeCalc]["shifts"])):
        print(employeeWorkWeekData[employeeCalc]["shifts"][x])
        print(weeklyHoursWorked)
    

while(running == True):
    employeeInUse = int(input("Enter Numbers: "))

    # Check if number is the correct length
    if(employeeInUse < 6 and employeeInUse > 6 and employeeInUse != -1):
        invalidFunction()
    # Check if the number is the correct number
    if(employeeInUse != -1 and employeeData[employeeInUse]["isClockedIn"] == False):
        clockIn()
            
    elif(employeeInUse != -1 and employeeData[employeeInUse]["isClockedIn"] == True):
        clockOut()
        
    elif(employeeInUse == -1):
        totalWeeklyHours()
