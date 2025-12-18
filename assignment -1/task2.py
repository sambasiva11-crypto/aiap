# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Ask user for input
user_input = input("Enter a string to reverse: ")
reversed_str = reverse_string(user_input)
print(f"Reversed string: {reversed_str}")