# Clock in and track work hours
from datetime import datetime
import sys

# Initializing Data
running = True

# Get and format the currewnt date and time
now = datetime.now()
dateAndTime = now.strftime("%d/%m/%y %H:%M")

# Intitializing Data Base
employeeData = {
    123456: {
        "name": "Justin Spanos",
        "isClockedIn": False,
        "clockedInDate": 0,
        },
    654321: {
        "name": "Natalia Spanos",
        "isClockedIn": False,
        "clockedInDate": 0,
        },
    111111: {
        "name": "Yo Momma",
        "isClockedIn": False,
        "clockedInDate": 0,
        }
    }

# For Later
employeeWorkWeekData = {
    123456: { "Empty"
        }
    }

# Functions
def invalidFunction():
    print("Invalid Number")

def clockIn():
    print()

def clockOut():
    print()

while(running == True):
    employeeInUse = int(input("Enter Numbers: "))

    # Check if number is the correct length
    if(employeeInUse < 6 and employeeInUse > 6):
        invalidFunction()
    # Check if the number is the correct number
    if(employeeData[employeeInUse]["isClockedIn"] == False):
        if employeeInUse in employeeData:
            employeeData[employeeInUse]["isClockedIn"] = True
            print()
            print("==================================")
            print("           Clocked In")
            print("        ", employeeData[employeeInUse]["name"])
            print("   Clocked in at:", dateAndTime)
            print("==================================")
            print()
            
    elif(employeeData[employeeInUse]["isClockedIn"] == True):
            employeeData[employeeInUse]["isClockedIn"] = False
            print()
            print("==================================")
            print("           Clocked Out")
            print("        ", employeeData[employeeInUse]["name"])
            print("   Clocked out at:", dateAndTime)
            print("==================================")
            print()

