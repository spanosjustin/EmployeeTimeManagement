# Clock in and track work hours
from datetime import datetime

def invalidFunction():
    print("Invalid Number")

# Get and format the currewnt date and time
now = datetime.now()
dateAndTime = now.strftime("%d/%m/%y %H:%M")

# Initializing variable
clockedIn = False

# Intitializing Data Base
employeeData = {
    123456: ["Justin Spanos"],
    654321: ["Natalia Gorney"],
    111111: ["Your Mom"],
    }

employeeData = {
    123456: {
        "name": "Justin Spanos",
        "isClockedIn": False,
        },
    654321: {
        "name": "Natalia Spanos",
        "isClockedIn": False,
        },
    111111: {
                "name": "Yo Momma",
        "isClockedIn": False,
        }
    }


employeeInUse = int(input("Enter Numbers: "))

# Check if number is the correct length
if(employeeInUse < 6 and employeeInUse > 6):
    invalidFunction()
# Check if the number is the correct number
if(clockedIn == False):
    if employeeInUse in employeeData:
        print()
        print("================")
        print("  Clocked In")
        print("      ", employeeData[employeeInUse]["name"])
        print("Clocked in at:", dateAndTime)
        print("================")
        clockedIn = True
elif(clockedIn == True):
    invalidFunction()

