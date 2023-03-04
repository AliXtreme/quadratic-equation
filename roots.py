# Importing module
import math

# Creating a function
def roots():
    print("\nFinding the roots of a quadratic equation of the form: ax^2 + bx + c = 0")
    # Inputs
    a = int(input("Value of a: "))
    b = int(input("Value of b: "))
    c = int(input("Value of c: "))
    print(f"\nYour quadratic equation is: ({a})x^2 + ({b})x + ({c})    Note:your values are written in parentheses")
    #User validate his input
    while True:
        user_input = input("\nIf your values is true press 'Y' to continue or any button to stop program: ")
        if user_input.lower() == 'y':
            break
        else:
            exit()
    # Define a discriminant
    d = b ** 2 - 4 * a * c
    # Solution
    if d > 0:
        x1 = -b/(2 * a) + math.sqrt(d)/(2 * a)
        x2 = -b/(2 * a) - math.sqrt(d)/(2 * a)
        print("\nSolution: ", round(x1, 5), "and", round(x2, 5))
    if d < 0:
        print("\nSolution: There is no valid root")
    if d == 0:
        x = -b/(2 * a) + math.sqrt(d)/(2 * a)
        print("\nSolution: ", round(x, 5))

roots() # Calling our function
