def count_vowels(string):
    """
    Count the number of vowels in a string.
    Args:
        string (str): The input string to check
    Returns:
        int: The count of vowels (a, e, i, o, u) - case insensitive
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
def count_vowels_short(string):
    """
    Count vowels using a more concise approach (one-liner style).
    """
    return sum(1 for char in string if char.lower() in "aeiou")
if __name__ == "__main__":
    print("=== Vowel Counter ===\n")
    user_input = input("Enter a string: ").strip()
    if not user_input:
        print("No input provided.")
    else:
        # Traditional approach (verbose)
        vowel_count_verbose = count_vowels(user_input)
        print(f"\nVerbose Method: '{user_input}' contains {vowel_count_verbose} vowel(s).")
        # Short approach (concise)
        vowel_count_short = count_vowels_short(user_input)
        print(f"Short Method: '{user_input}' contains {vowel_count_short} vowel(s).")
        # Verification
        print(f"\nBoth methods match: {vowel_count_verbose == vowel_count_short}")
        # Example test cases
        print("\n--- Test Cases ---")
        test_strings = ["Hello World", "Python", "AEIOU", "xyz"]
        for test in test_strings:
            print(f"'{test}' → {count_vowels_short(test)} vowel(s)")