# Complete this program to classify people by age
# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior
# Your code here:
age = int(input("Enter age: "))
if   age <=12:
    print("you is chid")
elif age <=19:
    print("you is Teenager")
elif age <=59:
    print("you is adult")
elif age >=60:
    print("you is senior")