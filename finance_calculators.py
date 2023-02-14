#Import math
import  math

'''
User should choose 'investment' or 'bond'
Return an error if neither is input

If 'investment':
Input the amount of money they are depositing
Input the interest rate
Input the years they are investing
Input 'simple' or 'compound' interest
Calculate and print the answer

If 'bond'
Input the present value of the house
Input the interest rate
Input how many months to repay the bond
Calculate and print the answer

 '''

print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print("")
print("Investment - to calculate teh amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")
print("")
calc_type = input("Input here: ")

calc_type = calc_type.capitalize()

print("")
print(f"You have chosen {calc_type.lower()}.")
print("")

#I wanted to make sure the user had a chance to change their answer should they get it wrong
if calc_type != "Investment" and calc_type != "Bond":
    calc_type = input("You must input either 'investment' or 'bond'. Please check your spelling" + '\n' + "Input here: ")

#user inputs their data
if calc_type == "Investment":
    initial_investment = round(float(input("How much money in R will you be investing? R")), 2)

if calc_type == "Investment":
    interest = float((input("What percentage is your interest rate? "))) / 100

if calc_type == "Investment":
    years = int(input("How many years will you be investing for? "))

if calc_type == "Investment":
    invest_type = input("Would you like to to invest using simple or compound interest? ")

#If the user chooses simple interest, calculate how much they will earn
if calc_type == "Investment" and invest_type.capitalize() == "Simple":
    interest_simple = round(initial_investment * (1 + (interest * years)), 2)

if calc_type == "Investment" and invest_type.capitalize() == "Simple":
    earnings = interest_simple - initial_investment

print("")

if calc_type == "Investment" and invest_type.capitalize() == "Simple":
    print(f"After {years} years, your initial investment of R{initial_investment} will earn R{earnings}. At the end of this period, it will be worth R{interest_simple}.")

#if the user chooses compound interest, calculate how much they will earn
if calc_type == "Investment" and invest_type.capitalize() == "Compound":
    interest_compound = round(initial_investment * math.pow((1 + interest), years), 2)

if calc_type == "Investment" and invest_type.capitalize() == "Compound":
    earnings = interest_compound - initial_investment

if calc_type == "Investment" and invest_type.capitalize() == "Compound":
    print(f"After {years} years, your initial investment of R{initial_investment} will earn R{earnings}. At the end of this period, it will be worth R{interest_compound}.")

#if the user chooses bond, input their data
if calc_type == "Bond":
    house_value = int(input("What is the value of your house? R"))

if calc_type == "Bond":
    interest = float((input("What percentage is your interest rate? "))) / 100

if calc_type =="Bond":
    interest = interest / 12

if calc_type == "Bond":
    months = int(input("How many months do you plan to take to repay the bond? "))

if calc_type == "Bond":
    bond_repay = round((interest*house_value)/(1 - (1 + (interest))**(-1 * months)), 2)

#Calculate how much the user would pay total
if calc_type == "Bond":
    bond_pay_total = bond_repay * months

if calc_type == "Bond":
    print("")
    
if calc_type == "Bond":
    print(f"Your monthly repayments on your R{house_value} house will be R{bond_repay}. Over the {months} months that you are repaying your bond, you will have paid R{bond_pay_total} total.")