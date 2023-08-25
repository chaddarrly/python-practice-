# *****************************************************************************
# ***************************  Python Source Code  ****************************
# *****************************************************************************
# 
#   DESIGNER NAME:  Chaddarrly Brown
# 
#       FILE NAME:  population
#  
#            DATE:  03/04/2021
#
# DESCRIPTION
#  this program will take the users input of starting population , growth percent, and years of growth
#  and calculate the final population for each year,then display the results in a table using
#
#    [final populationn = x(t), starting population = x(0), growth = r, time of growth = t]
#
#                           formula: x(t)= x(0)*(1 + r/100)**t
#
#
#
# *****************************************************************************
#------------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function will display the header and introduction to program
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#
# -----------------------------------------------------------------------------
def header_and_intro():
    print("welcome to the population increase program")
    print("-"*50)
    print()
    print("this program will display population growth over time")
    print()
# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function will convert the user population growth into a percentage
#
# INPUT PARAMETERS:
#   user_growth to calculate growth_percent
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   This function will return population growth as a percent
#
# -----------------------------------------------------------------------------
def get_growth_percent(user_growth):
    
    #variable used in this function
    growth_percent = 0.00
    
    growth_percent = user_growth / 100
    return (growth_percent)
# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function will calculate the final population using the user input of
#   starting population, population growth , and time of growth
#
# INPUT PARAMETERS:
#   none
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   This function will return final population calculation
#
# -----------------------------------------------------------------------------
def calc_population_growth(user_population, growth_percent, user_time):
    
    #variable used in the function
    final_population = 0.00
    
    final_population = user_population * (1 + growth_percent)**user_time
    return (final_population)
# -----------------------------------------------------------------------------
# DESCRIPTION
#   This function will get the user input for starting population, growth percent
#   and years of growth, then display the results in a table 
#
# INPUT PARAMETERS:
#   user_population, user_growth, and user_time
#
# OUTPUT PARAMETERS:
#   none
#
# RETURN:
#   none
#
# -----------------------------------------------------------------------------
def main():
    header_and_intro()
    
    #get user input 
    user_population = float(input("Enter starting population:"))
    user_growth     = float(input("Enter growth percent:"))
    user_time       = int(input("Enter years of growth:"))
    
    growth_percent  = get_growth_percent(user_growth)
    
    #print results in a table
    print()
    print("time \t population")
    print("------------------")
    
    
    for time in range(1,user_time + 1):
        print(time,"\t",round(calc_population_growth(user_population, growth_percent, time)))
    print()
    print("Program terminated")
    
# Call the main function. 
main() 
