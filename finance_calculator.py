import math
# program that calculates investments and bonds
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("investment   - to calculate the amount of interest you'll earn on investment")
print("bond     - to calculate the amount you'll pay on your home loan")
#ask user to input their selection
#add lower function to avoid errors
option = input("Enter your selection: ").lower() 

# if user selects investment
if option == "investment":
    # ask user to input values 
    deposit = float(input("Please enter the amount you would be depositing: "))
    rate = int(input("Enter the percentage of interest rate: "))
    years = int(input("Enter the number of years you'll be investing over: "))
    interest = input("Would you like simple or compound interest? ").lower()
    # user input divided by 100 to get percentage value
    rate = rate/100

    #formula for simple interest rounded down to 2 decimal places
    simple = round(deposit*(1 + rate * years),2) 
    #formula for compound interest rounded down to 2 decimal places
    compound = round(deposit * math.pow((1+rate),years),2) 
    # printing results based on whether simple or compound interest was chosen
    if interest == "simple":
        print(f"After {years} years you will have R{simple}")
    else:
        print(f"After {years} years you will have R{compound}")

# if statements for if bond option was selected
if option == "bond":
    # user enters inputs
    p_value = float(input("What is the present value of your house? "))
    rate = int(input("Enter the percentage of interest rate: "))
    # user inputfor rate divided by 100 and then 12 to get percentage value per month
    rate = rate/100/12
    months = int(input("Enter the number of months you'll be paying over: "))
    # formula for calculating bond
    payment = round((rate*p_value)/(1-(1+rate)**(-months)),2) 
    # final display of monthly payments
    print(f"You will pay R{payment} every month")