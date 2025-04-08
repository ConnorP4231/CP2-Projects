# Connor Pavicic, Financial Calculator
# This is a financial calculator with 5 options to choose from.

def saving_goal(): # This is the function for saving goal.
    try:
        #Savings goal calculator based on deposits.
        goal = int(input('Enter the amount you want to end with: '))
        deposit = int(input('Enter the amount you will deposit each month/week: '))
        deposit_rate = input('Will you deposit money every week or month? (week/month): ').lower()
        
        if deposit_rate == 'week': # The if statements that calculate what it going on.
            time = goal / deposit / 4  # Approximate weeks to months
        elif deposit_rate == 'month':
            time = goal / deposit
        else: # Checks to make sure that everything is valid.
            print("Invalid input for deposit rate. Assuming monthly deposits.")
            time = goal / deposit
        
        print(f"It will take approximately {time:.1f} months to reach your goal of ${goal}.\n") # The output of what the user input.
    except Exception as e:
        print(f'Error: {e}')

def compound_interest(): #The compound interest calculator function.
    try:
        #Compound interest calculator
        principal = float(input('How much money will you originally start with? ')) # The original amount
        rate = float(input('What is the annual interest rate (in %)? ')) / 100 # Percent of increase
        comp_frequency = int(input('How many times per year is the interest compounded? ')) # How often per year they are inputting money.
        time = float(input('For how many years will the money grow? ')) # How often per year they are inputting money.
        
        final_amount = principal * ((1 + rate / comp_frequency) ** (comp_frequency * time)) #All variables above are then put into the compound interest formula
        print(f"The final amount after {time} years will be ${final_amount:.2f}.\n") #The final output.
    except Exception as e:
        print(f'Error: {e}')

def budget_allocator(): #Budget allocator function.
    try:
        #Budget allocator.
        total_budget = float(input('Enter your total budget: ')) # The budget.
        categories = {} # The list for all the categories they want to allocate their money.
        
        while True:
            category = input('Enter a category name: ').capitalize()
            percent = float(input(f'What percentage of your budget would you like to allocate to {category}? '))
            # All this above is just asking for a category and how much money they want in it.
            
            if percent > 100 or percent < 0: # Making sure the user input isn't impossible.
                print("Invalid percentage. Please enter a value between 0 and 100.")
                continue
            
            categories[category] = percent
            
            more = input('Would you like to add another category? (yes/no): ').lower() #Asks the user if they want more categories.
            if more == 'no':
                break

        print("\nBudget Allocation Summary:")
        for category, percent in categories.items(): #The for loop that prints the categories, their percentage, and their allocation.
            allocation = (percent / 100) * total_budget
            print(f"{category}: {percent:.1f}% -> ${allocation:.2f}")
        print()
    except Exception as e:
        print(f'Error: {e}')

def sale_price(): #The sale price calculator function.
    try:
        #Sale price calculator.
        original_price = float(input('Enter the original price of the item: '))
        discount = float(input('Enter the discount percentage: ')) / 100
        final_price = original_price * (1 - discount) #The simple formula using the variables above to calculate the sale price.
        print(f"The discounted price is ${final_price:.2f}.\n") # Rounds the users answer to 2 decimal places.
    except Exception as e:
        print(f'Error: {e}')

def tip_calculator(): #Tip calculator function.
    try:
        #Tip calculator.
        bill = float(input('Enter the total bill amount: ')) # The amount they paid for whatever they got.
        service = input('Rate the service (good/decent): ').lower() # Tips can vary on customer experience.
        
        tip_rate = 0.2 if service == 'good' else 0.15 # If the service was decent then they get less.
        tip = bill * tip_rate
        total = bill + tip
        
        print(f"Tip: ${tip:.2f}")
        print(f"Total amount (bill + tip): ${total:.2f}\n")
        # All this above prints the tips and the total bill amount.
    except Exception as e:
        print(f'Error: {e}')

def financial_main(): #The main function that makes everything work.
    #Main menu for the financial calculator.
    while True: # While loop for as many uses as they want.
        choice = input("""
Select a calculator:
1. Savings goal calculator
2. Compound interest calculator
3. Budget allocator
4. Sale price calculator
5. Tip calculator
6. Exit

Enter your choice (1-6): """)
# All options listed including an exit feature to make sure the user can exit.

        if choice == '1':
            saving_goal()
        elif choice == '2':
            compound_interest()
        elif choice == '3':
            budget_allocator()
        elif choice == '4':
            sale_price()
        elif choice == '5':
            tip_calculator()
        elif choice == '6':
            print("Thank you for using the financial calculator. Goodbye!")
            break
        # Runs a function or a print statement based off what the user chose.
        else:
            print("Invalid choice. Please select a valid option.\n")
            # Makes sure that the user actually input a correct option.