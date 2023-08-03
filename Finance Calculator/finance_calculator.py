import math

invest_type = str("")
# I created the variable "invest_type" so there is a variable to start the loop
# once a condition is placed after the while function, I will redefine the variable

while invest_type != "investment" or invest_type != "bond":
    invest_type = str(input("Choose either 'investment' or 'bond' from the menu below\n\n"
                            "Investment - to calculate the amount of interest you'll earn on your investment\n"
                            "Bond - to calculate the amount you'll have to pay on a home loan\n"
                            "Enter here: ")).lower()
    # added lower after the fact to remove any capitalisation a user uses on their answer
    if invest_type != "investment" and invest_type != "bond":
        print("\nError: please enter the appropriate response to the question.\n")
    # this if statement means that if they do not enter the appropriate response,
    # they will continue to loop until they do

    # once they have selected bond, there are a number of questions they have to answer to get the right answer
    elif invest_type == "bond":
        # this loop is for anyone who picks bond
        house_value = float(input("What is the present value of your house? "))
        interest_rate2 = float(input("What is the annual interest rate? ").replace("%", ""))/100
        # the variable "interest_rate2" is to capture the interest rate of the bond
        # added replace incase someone puts a % sign in their answer and divided by 100 to change from percent to rate.
        bond_length = float(input("How many months do you plan to take to repay the bond? "))
        monthly_interest = interest_rate2 / 12
        # As the "interest_rate2" captures the annual interest rate, we need to find the monthly interest rate.
        # the variable "monthly_interest" is found by dividing "interest_rate2" by 12.

        bond_total = (monthly_interest * house_value)/(1 - (1 + monthly_interest)**(-bond_length))
        print(f"The monthly repayments on your bond will be {bond_total}")
        break # input a break to ensure it does not continue to run the loop

    # once they have selected investment, there are a number of questions they have to answer to get the right answer
    elif invest_type == "investment":
        # this loop is for anyone who picks investment
        money_invest = float(input("How much money are you depositing? "))
        interest_rate1 = float(input("What is the annual interest rate? ").replace("%", ""))/100
        # the variable "interest_rate1" is to capture the interest rate of the investment
        # added replace incase someone puts a % sign in their answer and divided by 100 to change from percent to rate.
        invest_length = float(input("How many years do you plan on investing? "))
        interest_type = str(input("Is this going to be compound or simple interest? ").lower())
        # added if statements so the code can determine which calculation to use when it is simple or compound interest.
        if interest_type == "simple" or interest_type == "simple interest":
            simple_total = money_invest * (1 + interest_rate1 * invest_length)
            print(f"The total you will have after {invest_length} years is {simple_total}")
        if interest_type == "compound" or interest_type == "compound interest":
            compound_total = money_invest * math.pow((1 + interest_rate1), invest_length)
            print(f"The total you will have after {invest_length} years is {compound_total}")
        break # input a break to ensure it does not continue to run the loop
