#!/usr/bin/env python3
#
#######################################################################################################
#
#
# TLDR: Run this script when contemplating an 'annutitized expense' (Netflix, Amazon Prime, 
# Cable TV, daily coffee, other recurring service).
#
# Written by Skip McGee, 20200824, for DJC2 20.2 AKA "The Looters"
# Solution script for the "goodies" left in expense_impact.py: adds some functionality and
# removes comments designed to help a new programmer understand the structure in expense_impact.py.
#
#
#######################################################################################################


error_number = 0 


def expense_input():
  try:
    global expense 
    expense = round(float(input("Enter an expense amount in dollars (example - 1.50): $")),2)
  except ValueError:
    print("Error while defining expense, please try again.")
    error_counter()
    expense_input()


def interval_input():
  try:
    global interval
    interval = int(input("Enter the expense recurrence time interval, Daily = 1, Weekly = 2, Monthly = 3, Yearly = 4: "))
  except ValueError:
    error_counter()
    print("Error while defining time interval, please try again.")
    interval_input()


def age_input():
  try:
    global age
    age = int(input("Enter your current age in years (example - 23): "))
  except ValueError:
    error_counter()
    print("Error while defining age, please try again.")
    age_input()


def interest_input():
  try:
    global interest_rate
    interest_rate = round(float(input("Enter your projected/anticipated after-tax real interest rate until age 60 (example - 5 or 6 percent: ")),2)
    interest_rate = round((interest_rate / 100),2)
  except ValueError:
    error_counter()
    print("Error while defining interest rate, please try again.")
    interest_input()


def inflation_input():
  try:
    global inflation
    inflation = round(float(input("Enter your best guess at your projected inflation rate until age 60 (example - 2 or 3 percent): ")),2)
    inflation = round((inflation / 100),2)
  except ValueError:
    error_counter()
    print("Error while defining inflation rate, please try again.")
    inflation_input()
    
    
def ret_input():
  try:
    global ret_age
    ret_age = round(float(input("Enter your planned retirement age: ")),2)
    ret_age = round((ret_age),2)
  except ValueError:
    error_counter()
    print("Error while defining retirement age, please try again.")
    ret_input()
  
  
def s_w_r():
  try:
    global swr
    swr = round(float(input("Enter your projected Safe Withdrawal Rate (example - 3 or 4 percent): ")),2)
    swr = round((100 / swr),2)
  except ValueError:
    error_counter()
    print("Error while defining retirement age, please try again.")
    s_w_r()
  
  
def input_cleaning():
  try:
    while expense <= 0:
      print("Please enter a number.")
      expense_input()
    while interval <= 0:
      print("Please enter an integer.")
      interval_input()
    while interval >= 5:
      print("Please enter an integer.")
      interval_input()
    while age <= 0:
      print("Please enter an age greater than 0")
      age_input()
    while age >= 120:
      print("Please enter an age less than 120, you probably are mentally", age)
      age_input()
    while interest_rate <= 0:
      print("Please enter an interest rate greater than 0")
      interest_input()
    while interest_rate >= 99:
      print("Please enter an interest rate less than 199%")
      interest_input()
    while inflation <= 0:
      print("Please enter an inflation rate greater than 0")
      inflation_input()
    while inflation >= 5:
      print("Please enter an inflation rate less than 500%")
      inflation_input()
    while swr >= 10:
      print("Please enter a realistic SWR under 10%")
      s_w_r()
    while swr <= 0:
      print("Please enter a realistic SWR greater than 0")
      s_w_r()
    while ret_age >= 110:
      print("Please enter a realistic retirement age less than 110")
      ret_input()
    while ret_age <= 18:
      print("Please enter a realistic retirement age greater than 18")
      ret_input()
  except:
    error_counter()
    errors(1)


def calcs():
  global current_value
  global future_value
  global interval_string
  global monthly_savings
  interval_string = ""
  compounding_years = (ret_age-age)
  try:
    if interval == 1:
      interval_string = "daily"
      current_value = (365.25 * expense) * swr
      current_value = round(current_value,2)
      future_value = round(current_value * ((1 + inflation) ** compounding_years),2)
    elif interval == 2:
      interval_string = "weekly"
      current_value = ((expense / 7) * 365.25) * swr
      future_value = round(current_value * ((1 + inflation) ** compounding_years),2)
    elif interval == 3:
      interval_string = "monthly"
      current_value = (expense * 12) * swr
      future_value = round(current_value * ((1 + inflation) ** compounding_years),2)
    elif interval == 4:
      interval_string = "yearly"
      current_value = expense * swr
      future_value = round(current_value * ((1 + inflation) ** compounding_years),2)
    nominal_inflation = (interest_rate + inflation + (interest_rate * inflation))
    monthly_savings = round(((((interest_rate/12) * future_value) / (1 + (interest_rate/12)**compounding_years) - 1)),2)
  except:
    error_counter()
    errors(2)
    

def output():
  first_line = f"The amount of money that you would need to fund a {interval_string} ${expense} expense from {age} years old until death is ${current_value}"
  second_line = f"The amount of money that you would need to fund a {interval_string} ${expense} expense (in current dollars) from {ret_age} years old until death is ${future_value}(in future dollars)."
  third_line = f"You would need to save ${monthly_savings} monthly until age 62 to be able to support your {interval_string} ${expense} expense (in current dollars) in retirement."
  print("*****")
  print("Script Output:")
  print(first_line)
  print(second_line)
  print("*****")
  print(third_line)
  print("*****")


def error_counter():
  global error_number
  error_number += 1


def errors(error=0):
  if error_number == 0:
    if error == 0:
      print("")
      return print("expense_impact-solution.py ran without errors")
  elif error_number >= 1:
    print("")
    print(error_number, "Error(s) occurred while defining the expense_impact.py script variables.")
    if error == 1:
      # GOODIE NUMBER 1: what should these error print statements say? Find where / under what conditions they are called and write print
      # statements to enable future troubleshooting.
      return print("Error with the input cleaning function.") # first print statement to create
    elif error == 2:
      return print("Error with the calculation function.") # second print statement to create
    elif error >= 3:
      return


def main():
  expense_input()
  interval_input()
  age_input()
  interest_input()
  inflation_input()
  ret_input()
  s_w_r()
  calcs()
  output()
  # GOODIE NUMBER 2: If the below argument did run, what error message would result and why? (NameError - variable/argument conflict)
  # After you figure it out, go ahead and remove the function call "errors(error_number)" below so your error print statements in GOODIE 1 could
  # execute appropriately (this will help in case you have problems with GOODIES 3 & 4)
  # Check out https://problemsolvingwithpython.com/07-Functions-and-Modules/07.07-Positional-and-Keyword-Arguments/
  # errors(error_number)
  
  
# GOODIE NUMBER 3: What if you wanted to retire at a different age than 62? Can you configure a new user input to allow a different retirement age?
# GOODIE NUMBER 4: What if you wanted to specify a different Safe Withdrawal Rate other than a yearly 4%? Can you create a new input for the user to be
# able to specify a SWR?


if __name__ == "__main__":
  main()
