# ...existing code...
def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (ignoring case, spaces and non-alphanumerics)."""
    normalized = ''.join(ch.lower() for ch in s if ch.isalnum())
    return normalized == normalized[::-1]

def main():
    text = input("Enter text to check for palindrome: ")
    if is_palindrome(text):
        print("Result: Palindrome")
    else:
        print("Result: Not a palindrome")

if __name__ == "__main__":
    main()
# ...existing code...