# Connor Pavicic, advanced_functions_notes

# 1. What is a helper function?
    # A helper function is a function that you write to call in another function. E.g. helper functions are used in your main function.
def is_int(user_input):
    try:
        int(user_input)
    except:
        print('Give me a number.')
        user_input = is_int(input('How old are you?:\n '))
    return user_input
    
def age():
    old = is_int(input('How old are you?: '))
    print(f"Cool. You are {old}.")

age()

# 2. What is the purpose of a helper function?
#   To make the code easier to read by sorting every task out into functions and then calling them later.
# 3. What is an inner function?
#   A function that exists inside of another function.
def add(a):
    b = int(input("Give me a number: "))

    def addition():
        print(a+b)

    addition()

add(3)
# 4. What is the scope of a variable in a function WITH an inner function?
#   The variable in the inner function has access to the outer variables since they are all local.
import logging

logging.basicConfig(level=logging.INFO)

def logger(func):

    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with {args}, {kwargs}")
        return func(*args, *kwargs)
    return wrapper

@logger
def adder(a,b):
    return a+b
print(adder(3,4))
# 5. Why do we use inner functions?
#   Less parameters, less returns, and less of a hassle. Also it has access to all of the outer functions' variables. (Stuff in the inner function cannot be accessed by the outer function).
# 6. What is a closure function?
#       Allows a function to remember and access variables from its lexical scope. A function that lets you remember values across multiple calls.
def add(a):
    
    def addition(b):
        return a+b

    return addition

base = add(10)

print(base(5))

#ANOTHER EXAMPLE
def math(income):

    def perc(amount, type):
        percent = amount/income
        print(f'Your {type} is ${amount}, and that is {percent} of your income.')
    return perc

def user_inputs(type):
    return int(input(f'What is your monthly {type}\n$'))

income = user_inputs("income")
rent = user_inputs("rent")
utilities = user_inputs("utilities")
groceries = user_inputs("groceries")
transportation = user_inputs("transportation")

start = 



# 7. Why do we write closure functions?
#   Because you can remember values across multiple calls.
# 8. What is recursion?
#   When you call a function inside of itself.
# 9. How does recursion work?
#   