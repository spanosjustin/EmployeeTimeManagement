# Clock in and track work hours
from datetime import datetime
from tkinter import *
import sys

master = Tk()
master.title("Time Management")
canvas_width = 600
canvas_height = 600

w = Canvas(master, width=canvas_width, height=canvas_height, bg="#000000")

w.pack()

# Initializing Data
running = True

# Get and format the currewnt date and time
now = datetime.now()
dateAndTime = now.strftime("%d/%m/%y %H:%M")
shiftHour = 0
shiftMinute = 0
totalShift = 0
weeklyHoursWorked = 0.00
userNumInput = []

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

def functioning():
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

# display screen
def display():
    ## number button
    def zeroClicked(*args):
        userNumInput.append(0)
        #w.delete(displayNum)
        #displayNum = w.create_text(170, 45, text=variable, font=("Helvetica", 26))
    
    #### NUMERICAL BUTTONS
    ## clock in
    w.create_rectangle(15, 500, 75, 575, outline="#36373b", fill="#36373b", tag="clockIn")
    w.create_text(45, 537, text="In", font=("Helvetica", 24), tags="clockIn")
    ## zero
    w.create_rectangle(100, 500, 160, 575, outline="#36373b", fill="#36373b", tag="zeroButton")
    w.create_text(130, 537, text="0", font=("Helvetica", 26), tags="zeroButton")
    ## clock out
    w.create_rectangle(185, 500, 245, 575, outline="#36373b", fill="#36373b", tag="clockOut")
    w.create_text(215, 537, text="Out", font=("Helvetica", 24), tags="clockOut")
    
    ## one
    w.create_rectangle(15, 400, 75, 475, outline="#36373b", fill="#36373b", tag="oneButton")
    w.create_text(45, 437, text="1", font=("Helvetica", 26), tags="oneButton")
    ## two
    w.create_rectangle(100, 400, 160, 475, outline="#36373b", fill="#36373b", tag="twoButton")
    w.create_text(130, 437, text="2", font=("Helvetica", 26), tags="twoButton")
    ## three
    w.create_rectangle(185, 400, 245, 475, outline="#36373b", fill="#36373b", tag="threeButton")
    w.create_text(215, 437, text="3", font=("Helvetica", 26), tags="threeButton")

    ####
    ## four
    w.create_rectangle(15, 300, 75, 375, outline="#36373b", fill="#36373b", tag="fourButton")
    w.create_text(45, 337, text="4", font=("Helvetica", 26), tags="fourButton")
    ## five
    w.create_rectangle(100, 300, 160, 375, outline="#36373b", fill="#36373b", tag="fiveButton")
    w.create_text(130, 337, text="5", font=("Helvetica", 26), tags="fiveButton")
    ## six
    w.create_rectangle(185, 300, 245, 375, outline="#36373b", fill="#36373b", tag="sixButton")
    w.create_text(215, 337, text="6", font=("Helvetica", 26), tags="sixButton")
    
    ####
    ## seven
    w.create_rectangle(15, 200, 75, 275, outline="#36373b", fill="#36373b", tag="sevenButton")
    w.create_text(45, 237, text="7", font=("Helvetica", 26), tags="sevenButton")
    ## eight
    w.create_rectangle(100, 200, 160, 275, outline="#36373b", fill="#36373b", tag="eightButton")
    w.create_text(130, 237, text="8", font=("Helvetica", 26), tags="eightButton")
    ## nine
    w.create_rectangle(185, 200, 245, 275, outline="#36373b", fill="#36373b", tag="nineButton")
    w.create_text(215, 237, text="9", font=("Helvetica", 26), tags="nineButton")

    ## number utility
    w.tag_bind("zeroButton","<Button-1>",zeroClicked)
    w.tag_bind("clockOut","<Button-1>",pointClicked)
    w.tag_bind("clockIn","<Button-1>",pointClicked)
    
    w.tag_bind("oneButton","<Button-1>",oneClicked)
    w.tag_bind("twoButton","<Button-1>",twoClicked)
    w.tag_bind("threeButton","<Button-1>",threeClicked)
    
    w.tag_bind("fourButton","<Button-1>",fourClicked)
    w.tag_bind("fiveButton","<Button-1>",fiveClicked)
    w.tag_bind("sixButton","<Button-1>",sixClicked)
    
    w.tag_bind("sevenButton","<Button-1>",sevenClicked)
    w.tag_bind("eightButton","<Button-1>",eightClicked)
    w.tag_bind("nineButton","<Button-1>",nineClicked)

display()

#while(running == True):

    
        
