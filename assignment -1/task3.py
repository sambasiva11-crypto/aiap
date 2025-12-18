# Recursive version of factorial function
def factorial_recursive(n):
    """Calculate factorial using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Iterative version of factorial function
def factorial_iterative(n):
    """Calculate factorial using iteration."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Ask user for input
try:
    num = int(input("Enter a number to find its factorial: "))
    
    print(f"\nRecursive Result: {num}! = {factorial_recursive(num)}")
    print(f"Iterative Result: {num}! = {factorial_iterative(num)}")
    
except ValueError:
    print("Please enter a valid integer.")