# ...existing code...
def fib_recursive(n: int) -> int:
    """
    Compute the nth Fibonacci number using plain recursion (0-indexed).
    fib_recursive(0) == 0, fib_recursive(1) == 1.
    Args:
        n: non-negative integer index
    Returns:
        int: nth Fibonacci number
    Raises:
        ValueError: if n is negative or not an int
    """
    # validate input
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    # base cases: return immediately for n==0 or n==1
    if n == 0:
        return 0
    if n == 1:
        return 1
    # recursive case: fib(n) = fib(n-1) + fib(n-2)
    return fib_recursive(n - 1) + fib_recursive(n - 2)
# Optional: small usage example when run as script
if __name__ == "__main__":
    # Example: 10th Fibonacci (0-indexed) -> 55
    print("fib_recursive(10) =", fib_recursive(10))
# ...existing code...