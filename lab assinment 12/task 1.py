def linear_search(lst, target):
    """
    Performs a linear search to find the index of a target value in a list.

    Parameters:
    lst (list): The list to search in.
    target : The value to search for.

    Returns:
    int: The index of the target if found, else -1.
    """
    for index, value in enumerate(lst):
        if value == target:
            return index  # Target found, return its index
    return -1  # Target not found

# Example usage
numbers = [10, 20, 30, 40, 50]
target_value = 30

index = linear_search(numbers, target_value)
if index != -1:
    print(f"Value {target_value} found at index {index}.")
else:
    print(f"Value {target_value} not found in the list.")
