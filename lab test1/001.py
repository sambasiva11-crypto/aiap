def get_positive_integer(prompt):
    while True:
        user_input = input(prompt)
        try:
            n = int(user_input)
            if n > 0:
                print(f"Accepted: {n}")
                return n
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def fibonacci_sequence(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# Main interaction
n = get_positive_integer("Enter the number of Fibonacci terms (positive integer): ")
fib_seq = fibonacci_sequence(n)
print("Fibonacci sequence:", fib_seq)
