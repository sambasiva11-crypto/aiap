def format_name(first_name, last_name):
    """
    Format a full name as "Last,First".
    Args:
        first_name (str): The person's first name
        last_name (str): The person's last name
    Returns:
        str: Formatted name as "Last,First"
    """
    return f"{last_name},{first_name}"
if __name__ == "__main__":
    print("Enter names for 3 people:")
    
    for i in range(1, 4):
        first = input(f"Enter first name {i}: ").strip()
        last = input(f"Enter last name {i}: ").strip()
        
        if not first or not last:
            print("Invalid input. Please enter both first and last names.")
        else:
            formatted = format_name(first, last)
            print(f"Formatted: {formatted}")
        print()