#Personal Finance Calculator
#Student: Tapanapong wongkaisron
#Date: 26/07/2568
#Purpose: Calculate monthly budget and savings

monthly_income = float(input("User's monthly income in (THB): "))
rent_cost = float(input("Monthly rent/housing cost: "))
food_budget = float(input("Monthly food budget in (THB): "))
transportation_cost = float(input("Monthly transportation expenses: "))
entertainment_budget = float(input("Monthly entertainment budget: "))
emergency_fund_percent = float(input("Percentage to save for emergency (e.g., 10.5): "))
investment_percent = float(input("Percentage to invest (e.g. 15.0): "))
#รับ input ข้อมูลจากผู้ใช้

Total_Fixed_Expenses = rent_cost + transportation_cost
Total_Variable_Expenses = food_budget + entertainment_budget
Total_Expenses = Total_Fixed_Expenses + Total_Variable_Expenses
Remaining_Income = monthly_income - Total_Expenses
Emergency_Fund_Amount = monthly_income * (emergency_fund_percent / 100)
Investment_Amount = monthly_income * (investment_percent / 100)
Available_for_Savings = Remaining_Income - Emergency_Fund_Amount - Investment_Amount

Expense_Ratio = (Total_Expenses / monthly_income) * 100
#เป็นที่คำนวนข้อมูลที่ได้รับมาจากการ input

print("\n=== MONTHLY BUDGET REPORT ===")  # รายงานงบประมาณรายเดือน
print(f"Income: {monthly_income:.2f} THB")  # แสดงรายได้ต่อเดือน
print(f"Fixed Expenses: {Total_Fixed_Expenses:.2f} THB")  # แสดงค่าใช้จ่ายคงที่
print(f"Variable Expenses: {Total_Variable_Expenses:.2f} THB")  # แสดงค่าใช้จ่ายผันแปร
print(f"Total Expenses: {Total_Expenses:.2f} THB")  # แสดงค่าใช้จ่ายทั้งหมด
print(f"Remaining: {Remaining_Income:.2f} THB")  # แสดงรายได้ที่เหลือ

print("\n=== SAVINGS BREAKDOWN ===")  # แสดงรายละเอียดเงินเก็บออม
print(f"Emergency Fund ({emergency_fund_percent}%): {Emergency_Fund_Amount:.2f} THB")  # แสดงจำนวนเงินสำหรับกองทุนฉุกเฉิน
print(f"Investments ({investment_percent}%): {Investment_Amount:.2f} THB")  # แสดงจำนวนเงินสำหรับการลงทุน
print(f"Available for Savings: {Available_for_Savings:.2f} THB")  # แสดงจำนวนเงินที่สามารถเก็บออมได้

print("\n=== ANALYSIS ===")  # วิเคราะห์งบประมาณ
print(f"Expense Ratio: {Expense_Ratio:.2f}%")  # คำนวนสัดส่วนค่าใช้จ่ายต่อรายได้
