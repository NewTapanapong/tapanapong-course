"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
Quiz = input("pls you choice 1 THB to USD, 2 USD to THB: ")
number =float(input("number: "))
if Quiz == "1":
    print(F"{number} THB = {number/35.5} USD")
if Quiz =="2":
    print(F"{number} USD = {number*35.5} THB ")
     