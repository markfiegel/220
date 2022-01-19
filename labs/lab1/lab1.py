"""
Mark Fiegel
lab1.py
I made a program that determines the monthly interest rate
I certify that this assignment is entirely my own work.
"""

def monthly_interest():
     average_rate = eval(input("What is your annual interest rate?    "))
     average_rate_percent= average_rate/100
     days_billing_cycle =  eval(input("How long is your billing cycle?    "))
     prev_balance = eval(input("what is your previous balance?    "))
     payment_amt = eval(input("How much are you paying?    "))
     cycle_day = eval(input("What day do you make your payment?    "))
     step1 = prev_balance * days_billing_cycle
     step2 = payment_amt * (days_billing_cycle-cycle_day)
     step3 = step1 - step2
     avg_daily_bal = step3/days_billing_cycle
     monthly_rate = average_rate_percent/12
     monthly_interest_rate = avg_daily_bal*monthly_rate
     monthly_interest_rate = round(monthly_interest_rate, 2)
     print("This is your total monthly interest $", monthly_interest_rate)




monthly_interest()