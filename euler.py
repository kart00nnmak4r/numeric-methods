import math

# Allow the user to input the differential equation as a string and dynamically evaluate it.
# This makes the code flexible for solving various differential equations.
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

# Método de Euler
def euler_method(f, x0, y0, h, x_end):
    """
    Resuelve una EDO utilizando el método de Euler.

    Parámetros:
        f: función que representa dy/dx = f(x, y).
        x0: valor inicial de x.
        y0: valor inicial de y.
        h: tamaño del paso.
        x_end: valor final de x hasta donde se resolverá.

    Retorna:
        Una lista de pares (x, y) que representan la solución aproximada.
    """
    results = [(x0, y0)]  # Lista para almacenar los puntos (x, y)
    x, y = x0, y0

    while x < x_end:
        try:
            y = y + h * f(x, y)  # Actualización de y según el método de Euler
        except ValueError as e:
            print(f"Error en x = {x:.4f}, y = {y:.4f}: {e}")
            break  # Detener el cálculo si ocurre un error
        x = x + h
        results.append((x, y))

    return results

# Solicitar al usuario los parámetros
print("Método de Euler para resolver ecuaciones diferenciales")
print("Ingrese la ecuación diferencial en términos de x y y, por ejemplo, 'math.sqrt(x + y)' para dy/dx = sqrt(x + y).")
equation = input("Ingrese la ecuación diferencial: ")
try:
    x0 = float(input("Ingresa el valor inicial de x (x0): "))  # Valor inicial de x
    y0 = float(input("Ingresa el valor inicial de y (y0): "))  # Valor inicial de y
    h = float(input("Ingresa el tamaño del paso (h): "))  # Tamaño del paso
    x_end = float(input("Ingresa el valor final de x: "))  # Valor final de x
except ValueError:
    print("Entrada inválida. Por favor, ingrese valores numéricos.")
    exit()

# Convertir la ecuación ingresada por el usuario en una función
differential_equation = parse_equation(equation)

# Resolver la EDO con el método de Euler
try:
    solution = euler_method(differential_equation, x0, y0, h, x_end)
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Imprimir los resultados
print("\nSolución aproximada (Método de Euler):")
for x, y in solution:
    print(f"x = {x:.4f}, y = {y:.4f}")

