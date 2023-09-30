import sys

#You have decided to use the ATM in XYZ bank instead of going to one of the tellers
#You are given a variety of options, and it is up to you to interact with the ATM in
#You are able to deposit, withdraw, and view your balance

def welcome():
    #Welcome message
    print("Welcome to XYZ Bank today. In order to proceed, please enter your debit card.")
    
    #Ask user to insert debit card
    insert = input("Will you insert your debit card? (yes/no): ")
    
    #Determine whether or not the customer would like to proceed
    if insert.lower().strip() == 'yes':
        print("Thank you for inserting your debit card.")
        insert_pin()
    else:
        print("No problem, have a great day.")

def insert_pin():
    #Can change correctPin to any 4-digit number
    correctPin = 9876
    attempts = 3

    #After 3 attempts the customer will be locked out
    while attempts > 0:
        pinNum = input("What is your 4-digit PIN number?: ")
        if int(pinNum) != correctPin:
            attempts -= 1
            print(f"You have {attempts} attempts left before your card is locked.")

        #When the customer enters the correct PIN they proceed to the next step
        else:
            action(0, firstVisit = True)  # Start with a balance of 0, can alter starting balance

    #The customer guessed incorrectly, will have to rerun the file
    print("Your debit card has been locked, please call ***-***-**** in order to unlock it.")
    sys.exit()

#Lets the customer determine what they'd like to do
def action(balance, firstVisit):
    if firstVisit == True:
        furtherDecision = 'yes'

    #If it is not the first time the customer encounters this screen
    #They will be given options of what they can do
    else:
        print("You have been returned to the home screen")
        furtherDecision = input("Would you like to do something else? (yes/no): ")
    
    #If the customer wants to continue, they proceed to the next step 
    if furtherDecision.lower().strip() == 'yes':
        nextAction = input("Press: 1 for deposit, 2 for withdrawal, 3 for balance amount, 4 to exit: ")
        if nextAction.strip() == '1':
            deposit(balance)
        elif nextAction.strip() == '2':
            withdraw(balance)
        elif nextAction.strip() == '3':
            reveal_balance(balance)
        
        #The customer has chosen to leave the ATM
        elif nextAction.strip() == '4':
            print("You have chosen to exit, have a great day.")
            sys.exit()
        
        #The customer submitted an invalid input, prompts them again
        else:
            print("Invalid choice. Please choose a valid action.")
            action(balance, firstVisit=False)
    else:
        print("You have chosen not to pursue further actions, have a great day.")

#Allows the user to deposit money
def deposit(balance):
    amount = int(input("Enter the USD amount that you'd like to deposit: "))

    #The USD amount has to be greater than 0
    if amount >= 0.01:
        pass
    else:
        print("You cannot deposit amounts that are less than $0.01")
        action(balance, firstVisit=False)

    #Confirms the amount with the customer
    decision = input(f'Are you sure you want to deposit ${amount}? (yes/no): ')

    #If the customer confirms, the amount is added to their balance 
    if decision.strip().lower() == 'yes':
        balance += amount
        print(f'Your new balance is ${balance}')
    
    #Otherwise they return to the homescreen of options
    else:
        print('You have chosen not to deposit.')
    action(balance, firstVisit=False)

#Allows the user to withdraw money
def withdraw(balance):
    #Displays their balance
    print(f'Your current balance is ${balance}')

    #The withdraw amount has to be greated than 0
    amount = int(input("How much would you like to withdraw?: "))
    if amount >= 0.01:
        pass
    else:
        print("You cannot withdraw amounts that are less than $0.01")
        action(balance, firstVisit=False)
    
    #Confirms the amount with the customer
    decision = input(f'Are you sure you want to withdrawal ${amount}? (yes/no): ')
    if decision.strip().lower() == 'yes':

        #If the amount is available to withdraw, it is done
        if amount <= balance:
            balance -= amount
            print(f"You have succesfully withdrawn ${amount}")
            print(f'Your new balance is ${balance}')
        
        #If they do not have the available amount to withdraw, they are returned to the home screen
        else:
            print("You cannot withdraw an amount greater than your balance.")
    else:
        print('You have chosen not to withdraw.')
    action(balance, firstVisit=False)

#Allows the customer to view their balance
def reveal_balance(balance):
    print(f'Your current balance is ${balance}')
    action(balance, firstVisit=False)

welcome()
