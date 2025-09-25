"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("PERSONAL INFORMATION VALIDATOR")
Name = input("Enter your name: ")
age = int(input("Enter your age: "))
phone = input("Enter your phonenumber: ")
Name_validator = True
for char in Name:
    if char.isalpha():
        Name_validator = True
    else:
        Name_validator = False
age_validator = True
if 18<=age and age<=65:
    age_validator = True
else:
    age_validator = False

if len(phone)!=10:
    print("Error")
phone_validator = True
for char in phone:
    if char.isdigit():
        phone_validator = True
    else:
        phone_validator = False

print("Validation Results")
if Name_validator == True:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid")
if age_validator == True:
    print(f"age: Valid({age} years old)")
else:
    print("age: Invalid")
if phone_validator == True:
    print("phone:Valid (10-digit number)")
else:
    print("phone:Invalid")

print("Formatted Information")
if Name_validator == True:
    print(f"Name: {Name.upper()}")

if age_validator == True:
    print("Age Group: Young Adult (18-30)")

if phone_validator == True:
    print(f"phone: +66-{phone[1:]}")