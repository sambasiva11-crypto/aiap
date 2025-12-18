# ...existing code...

def find_max(numbers):
    """Return the largest number in a list. Raises ValueError if list is empty."""
    if not numbers:
        raise ValueError("List is empty.")
    return max(numbers)

def parse_input(s):
    """Parse a string of numbers separated by spaces or commas into a list of numbers."""
    parts = s.replace(',', ' ').split()
    nums = []
    for p in parts:
        try:
            if '.' in p:
                nums.append(float(p))
            else:
                nums.append(int(p))
        except ValueError:
            raise ValueError(f"Invalid number: {p}")
    return nums

def main():
    s = input("Enter numbers separated by space or comma: ").strip()
    try:
        nums = parse_input(s)
        print(f"Largest number: {find_max(nums)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

# ...existing code...