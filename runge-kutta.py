# Runge-Kutta Second Order Method (RK2)
# This program solves differential equations using RK2.

# Step 1: Import necessary libraries
# Libraries are like tools. We need 'matplotlib' to draw graphs and 'numpy' for calculations.
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Define the differential equation
# The user will input the differential equation as a string.
# We will use Python's eval() function to evaluate it dynamically.
def parse_equation(equation):
    """
    Converts a user-defined equation into a Python function.
    Parameters:
    equation: A string representing the equation, e.g., "x + y" for dy/dx = x + y.

    Returns:
    A Python function that computes dy/dx given x and y.
    """
    def equation_function(x, y):
        return eval(equation)
    return equation_function

# Step 3: Define the Runge-Kutta function
# This function calculates values using the RK2 method.
def runge_kutta_2nd_order(f, x0, y0, x_end, h):
    """
    Parameters:
    f: The differential equation function (dy/dx = f(x, y))
    x0: The starting value of x
    y0: The starting value of y (initial condition)
    x_end: The ending value of x
    h: The step size (how much we move forward in each calculation)

    Returns:
    x_values: List of x values
    y_values: List of y values corresponding to x_values
    """
    # Initialize lists to store x and y values
    x_values = [x0]
    y_values = [y0]

    # Loop to calculate y at each step until we reach x_end
    while x0 < x_end:
        # Calculate the intermediate slope (k1) at the start of the interval
        k1 = h * f(x0, y0)

        # Calculate the slope (k2) at the midpoint of the interval
        k2 = h * f(x0 + h / 2, y0 + k1 / 2)

        # Update y using k2
        y0 = y0 + k2

        # Move x to the next step
        x0 = x0 + h

        # Store the new x and y values
        x_values.append(x0)
        y_values.append(y0)

    return x_values, y_values

# Step 4: Input parameters
# Allow the user to input the differential equation, starting values, and step size for our calculation.
print("Runge-Kutta 2nd Order Method to Solve Differential Equations")
print("Enter the differential equation in terms of x and y, e.g., 'x + y' for dy/dx = x + y.")
equation = input("Enter the differential equation: ")
try:
    x0 = float(input("Enter the initial x value (x0): "))  # Starting x value
    y0 = float(input("Enter the initial y value (y0): "))  # Starting y value (initial condition)
    x_end = float(input("Enter the ending x value (x_end): "))  # Ending x value
    h = float(input("Enter the step size (h): "))  # Step size (smaller step size gives more accurate results)
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

# Convert the user input equation into a function
differential_equation = parse_equation(equation)

# Step 5: Solve the equation using RK2
x_values, y_values = runge_kutta_2nd_order(differential_equation, x0, y0, x_end, h)

# Step 6: Plot the results
# We use a graph to show how y changes as x increases.
plt.plot(x_values, y_values, label="RK2 Solution", marker="o")
plt.title(f"Solving dy/dx = {equation} using RK2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

# Show the plot without blocking program execution
plt.show(block=False)
plt.pause(1)  # Pause to ensure the plot is displayed briefly before moving on

# Step 7: Print results
# Display the values of x and y for each step in the terminal.
print("x values:", x_values)
print("y values:", y_values)

# Keep the plot window open until the user closes it
plt.show()

