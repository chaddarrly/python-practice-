# *****************************************************************************
# ***************************  Python Source Code  ****************************
# *****************************************************************************
# 
#   DESIGNER NAME:  Chaddarrly Brown
# 
#       FILE NAME:  leap_year
#  
#            DATE:  03/11/2021
#
# DESCRIPTION
#  This program will take the users input of years (YYYY), and display
#  if that year is a leap year or not. the program will run until user
#  choose to exit
#
#
# *****************************************************************************
#---------------------------------------------------
# Variables to be used in program
#---------------------------------------------------
year = 0.0
#---------------------------------------------------
#header and introduction message
print("welcome to the leap year program")
print("-"*40)
print()
print("This program will tell you if the year(YYYY)\n"
       + "entered is a leap year")
print()

#loop if else statement
while True:
    
    #get user input
    year = int(input("Enter a year (YYY), or press 0 to exit program: "))
    
    #if statement to find leap year
    if year == 0:
        print("Program terminated")
        print()
        break
    
    elif year < 0 or year < 100:
        print("Error, invalid response")
        print()
        
    elif year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
        print("Febuary",year, "is a Leap Year and has 29 days")
        print()
        
    else:
        print("Febuary",year, "is not a Leap Year")
        print()



