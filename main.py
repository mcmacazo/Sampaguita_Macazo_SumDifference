#======================================================================================================================
# PROGRAMMER: MACAZO, MIESHA DENISE C.
# SECTION: 8 - SAMPAGUITA
# ACTIVITY 2:  Functions and Modular Programming in Python - SUM and DIFFERENCE CALCULATOR
#======================================================================================================================

# SUM CALCULATOR

num1 = float(input("Enter a number: "))
num2 = float(input("Enter second number: "))

def calculate_sum():
    global num1, num2
    total = num1 + num2
    print("Sum:", total)

# DIFFERENCE CALCULATOR

def calculate_difference():
    total = num1 - num2
    print("Difference:", total)

#OUTPUT

calculate_sum()
calculate_difference()




