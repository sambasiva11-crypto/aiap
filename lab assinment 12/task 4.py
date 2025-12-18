def f(x):
    return 2 * x**3 + 4 * x + 5

def df(x):
    return 6 * x**2 + 4

# User Inputs
x = float(input("Enter initial guess for x: "))
learning_rate = float(input("Enter learning rate (e.g., 0.001): "))
min_x = float(input("Enter minimum allowed x (e.g., -10): "))
precision = 1e-7
max_iters = 10000

for i in range(max_iters):
    prev_x = x
    x = x - learning_rate * df(x)
    if x < min_x:
        x = min_x
        break
    if abs(x - prev_x) < precision:
        break

print(f"The value of x at minimum (bounded by user input): {x}")
print(f"The minimum value of f(x): {f(x)}")
