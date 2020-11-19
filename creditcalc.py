from math import log, ceil
import sys

parameters = sys.argv

# placeholders for input:
type_ = ""
principal = 0
payment = 0
periods = 0
interest = 0
for parameter in parameters:
    if "--type=" in parameter:
        type_ = parameter.replace("--type=", "")
    if "--principal=" in parameter:
        principal = float(parameter.replace("--principal=", ""))
    if "--payment=" in parameter:
        payment = float(parameter.replace("--payment=", ""))
    if "--periods=" in parameter:
        periods = int(parameter.replace("--periods=", ""))
    if "--interest=" in parameter:
        interest = float(parameter.replace("--interest=", ""))

# functions:
def periods_calc(P, A, r):
    i = r / (100 * 12)
    X = A / (A - i * P)
    n = ceil(log(X, 1 + i))
    years = n // 12
    months = n % 12
    print(f'It will take {years} years and {months} months to repay this loan!')
    overpayment = round(P - n * A)
    print(overpayment)
def monthly_calc(P, n, r):
    i = r / (100 * 12)
    X = i * pow((1 + i), n) / (pow((1 + i), n) - 1)
    A = ceil(P * X)
    print(f'Your monthly payment = {A}!')
    overpayment = round(n * A - P)
def principal_calc(A, n, r):
    i = r / (100 * 12)
    X = i * pow((1 + i), n) / (pow((1 + i), n) - 1)
    P = A / X
    print(f'Your loan principal = {round(P)}!')
    overpayment = round(n * A - P)
    print(overpayment)
def diff_calc(P, n, r):
    i = r / (100 * 12)
    sum_ = 0
    for m in range(n):
        X = ceil(P / n + i * (P - P * m / n))
        sum_ += X
        print(f'Month {m + 1}: payment is {X} ')
    overpayment = ceil(sum_ - P)
    print()
    print(overpayment)

# conditions
if len(parameters) < 5:
    print("Incorrect parameters")
elif type_ == "" or interest == 0:
    print("Incorrect parameters")
elif type_ == "diff" and payment != 0:
    print("Incorrect parameters")
elif principal < 0 or payment < 0 or periods < 0 or interest < 0:
    print("Incorrect parameters")
else:
# calculations
    if type_ == "annuity":
        if principal == 0:
            principal_calc(payment, periods, interest)
        elif payment == 0:
            monthly_calc(principal, periods, interest)
        elif periods == 0:
            periods_calc(principal, payment, interest)
    if type_ == "diff":
        diff_calc(principal, periods, interest)
