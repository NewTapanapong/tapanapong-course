# Complete this ATM simulation
balance = 10000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = int(input("Choose option: "))
        
        # Complete the menu logic here
        # Your code here:
        if choice == 1:
         print("balance is:",balance)
        elif choice == 2:
           monney = float(input("withdraw is:"))
           balance = balance - monney
           print("you have: ",balance)
        elif choice == 3:
           DP = float(input("Desposit is: "))
           balance = balance + DP
           print("you have: ",balance)
        elif choice == 4:
           print("thank you")
           break
else:
    print("Invalid PIN")