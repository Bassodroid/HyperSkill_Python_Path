# write your code here
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", action='store_const')
parser.add_argument("--payment",type=float, default=0, help="The amount paid monthly on the loan" )
parser.add_argument("--interest",type=float, default=0, help="The interest rate of the loan" )
parser.add_argument("--periods",type=int, default=0, help="The total amount of time needed to repay the loan in months" )
parser.add_argument("--principal", type=float, default=0, help="The initial amount borrowed")
args = parser.parse_args(exit_on_error=False)
type = args.type
principal = args.principal
periods = args.periods
interest = args.interest
payment = args.payment

try:
    if type == "annuity":
        if payment > 0 and principal > 0 and interest > 0:
            interest = interest / (12 * 100)
            periods = payment / (payment - interest * principal)
            base = 1 + interest
            repayment_period_months = math.ceil(math.log(periods, base))
            if repayment_period_months % 12 == 0:
                repayment_period_years = repayment_period_months // 12
                print(f"It will take {repayment_period_years} years to repay this loan!")
            elif repayment_period_months % 12 != 0:
                repayment_period_years = repayment_period_months // 12
                remaining_months = repayment_period_months % 12
                print(f"It will take {repayment_period_years} years and {remaining_months} months to repay this loan!")
        elif principal > 0 and interest > 0 and periods > 0:
            interest = interest / (12 * 100)
            a = interest * math.pow((1 + interest), periods)
            b = math.pow((1 + interest), periods) - 1
            payment = math.ceil(principal * a / b)
            print(f"Your monthly payment = {payment}")
        elif payment > 0 and periods > 0 and interest > 0:
            interest = interest / (12 * 100)
            a = interest * math.pow((1 + interest), periods)
            b = math.pow((1 + interest), periods) - 1
            x = a / b
            principal = payment / x
            print(f"Your loan principal = {principal}!")
try:
    if type == "diff" and payment == 0 and interest > 0 and principal > 0 and periods > 0:



'''def loanCalculator(): # define Loan Calculator as a function
    principal_amount = float(input("Enter the loan principal: ")) # Request principal, total amount borrowed.
    user_option = input("""What do you want to calculate?\n type "m" - for number of monthly payments,
     type "p" - for the monthly payment: """) # provide option to calculate monthly payments or months needed to until repayment
    if user_option == "m": # if user selects m, calculate months until repayment
        monthly_payment = float(input("Enter the monthly payment: "))
        months_until_repayment = math.ceil((principal_amount / monthly_payment))
        print(f"It will take {months_until_repayment} months to repay the loan")
    elif user_option == "p": # if user selects p, calculate monthly payments rounded to nearest ones and final months payment
        repayment_months = int(input("Enter the number of months: "))
        if principal_amount % repayment_months == 0:
            payment_amount = principal_amount / repayment_months
            print(f"Your monthly payment = {payment_amount}")
        elif principal_amount % repayment_months != 0:
            rounded_payments = math.ceil((principal_amount / repayment_months))
            last_payment = principal_amount - (repayment_months - 1) * rounded_payments
            print(f"Your monthly payment = {rounded_payments} and the last payment = {last_payment}.")

loanCalculator()'''