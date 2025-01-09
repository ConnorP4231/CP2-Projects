# Connor Pavicic, Financial Calculator
# This is a financial calculator

# goal = int(input('Enter the number that you amount to end with: '))
# deposit = int(input('Enter the number that you will deposit each month/week: '))
# deposit_rate = input('Will you deposit money every week or month?: ').lower()

compound_inital = int(input('How much money will you originally start with?: '))
compound_increase = (int(input('What percent do you want to have your money increase by?: '))/100)
compound_frequency = int(input('How many times per year will you receive money?: '))
compound_time = int(input('How many years do you want to want to have this going?: '))

# def saving_goal(goal=goal, deposit=deposit):
    # time = goal/deposit
    # return time

def compound_interest(compound_inital = compound_inital, compound_increase = compound_increase, compound_time = compound_time):
    final_amount = (compound_inital*(((1+(compound_increase/compound_time))^(compound_frequency*compound_time)))) #formula is not working
    return final_amount


print(compound_interest())