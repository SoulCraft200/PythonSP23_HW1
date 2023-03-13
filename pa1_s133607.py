"""
Name:Sulaiman Khalifa Khalfan Al Yousfi
ID:s133607
Assignment: PA1
Purpose: Write a program the calculates the equal monthly installment(EMI) for Bank Muscat Al Jawhara type customers.
Input: 1 AccountNumber(aNum) sting
       2 Amount of loan (aLn) int
       3 Interest Rate (r) float
       4 Number of years (yrs) int
Output: a table of all the variables + eMI
Algorithm: 1.Prompt the user for the wanted inputs.
           2.Check weather the input is a 15 char and ends with 2 letters.
           3.If the input doesn't pass the check print reason and exist the program.
           4.If the input passes the check then, calculate EMI using the given formula and covert years to month and
             annual to monthly interest rate.
           6.Display the results in a format of a table.
Test:
Round1:
    input:
        Account Number = 1234567891011AA
        years = 5
        Loan = 30000
        Rate = 5
    Output:
        Monthly Interest rate = 0.00417
        Number of months = 60
        Equal monthly installment EMI = 566.13701

Round2
    Input:
        Account Number = 123456789AA
    Output:
        "For non-Al Jawhara accounts, other procedures will be followed to find EMI....."

"""
from sys import exit
# Promoting the user for the account number.
aNum = input("Input the account number: ")

# Checking weather the inputs is correct or not.
if len(aNum) == 15 and aNum[-1].isalpha() and aNum[-2].isalpha():

    # Prompting the user for the rest of the input variables.
    yrs = int(input("Input Number of years of the loan: "))
    aLn = int(input("Input Amount of the loan: "))
    r = float(input("Input Annual bank interest rate: "))

    # Converting
    months = yrs * 12
    mRate = (r/12)/100

    # Calculating EMI
    eMI = aLn * mRate * ((1 + mRate) ** months) / ((1 + mRate) ** months - 1)

    # Display results
    print("%-25s%-25s%-25s" % ("Monthly interest rate", "Number of months", "Equal monthly installment EMI"))
    print("*" * 90)
    print("%-25.5f%-25d%-25.5f" % (mRate, months, eMI))
else:
    # Exit program
    exit("For non-Al Jawhara accounts, other procedures will be followed to find EMI.....")
