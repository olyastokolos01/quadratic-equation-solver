import math

def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c  # Обчислення дискримінанта
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return x1, x2
    elif d == 0:
        x = -b / (2*a)
        return x,
    else:
        return "No real roots"

# Введення коефіцієнтів
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Розв’язання рівняння
solution = solve_quadratic(a, b, c)
print("Solution:", solution)
