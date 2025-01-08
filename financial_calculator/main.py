# Connor Pavicic, Financial Calculator
# This is a financial calculator

def saving_goal():
    goal = int(input('Enter the number that you amount to end with: '))
    deposit = int(input('Enter the number that you will deposit each month/week: '))
    deposit_rate = input('Will you deposit money every week or month?: ').lower()

    time = goal/deposit

    if deposit_rate == 'week':
        print(f'You meet your goal after {time} weeks.')
    else:
        print(f'You will meet your goal after {time} months. ')


saving_goal()