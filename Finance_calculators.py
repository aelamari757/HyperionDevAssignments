import math
# Investment Section
# Used triple single quotes for clearer reading

_Select_Option = input('''Investment: calculates the amount of interest you'll earn on your investment. 
Bond: calculates the amount you'll have to pay on a home loan. 
In order to proceed, please enter either 'Investment' or 'Bond' from the menu above ''')

# This will ensure that no case-sensitive error occurs when user inputs
_Select_Option = _Select_Option.lower() 

# This will ensure that any other word picked outside of investment or bond will result in an error
if _Select_Option not in ["investment", "bond"]:
    print("Error: Invalid option. Please enter either 'Investment' or 'Bond'.")
else:
    print(f"You have selected: {_Select_Option}") 

if _Select_Option == "investment":
    P = float(input("Enter amount that is being deposited: "))

    interest_rate_input = input("Enter the interest rate (e.g., 30% for 30%): ")
    
    # Checks to esnure output is a % regardless of input
    if '%' in interest_rate_input:
        r = float(interest_rate_input.replace('%', '')) / 100
    else:
        r = float(interest_rate_input) / 100

    t = int(input("Enter the number of years you plan to invest: "))
    interest_type = input("Would you like simple or compound interest? ").lower()

# If statement here must be indented to ensure the code runs without error from previous lines
    if interest_type == "simple":
        A = P * (1 + r * t)
        print(f"The total amount after {t} years with simple interest is: ${A:.2f}") # curly brackets used to insert variables

    elif interest_type == "compound":
        A = P * math.pow((1 + r), t)
        print(f"The total amount after {t} years with compound interest is: ${A:.2f}") 

# Adding an else option to ensure user selects from given options
    else:
        print("Invalid interest type. Please choose either 'simple' or 'compound'.")

# Bond section 

elif _Select_Option == "bond": 
    P = float(input("Enter the present value of the house: "))
    annual_rate = float(input("Enter the annual interest rate "))
    n = int(input("Enter the number of months you plan to repay the bond: "))  

    i = (annual_rate / 100) / 12
    repayment = (i * P) / (1 - (1 + i) ** -n)

    print(f"Your monthly repayment is: ${repayment:.2f}")