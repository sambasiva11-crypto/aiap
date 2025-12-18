def bubble_sort(arr):
    """
    Sorts a list in ascending order using the Bubble Sort algorithm.
    
    Parameters:
    arr (list): The list to sort.
    
    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Track if any swaps are made in this pass
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps were made, the list is already sorted
        if not swapped:
            break
    return arr

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers.copy())

print("Original list:", numbers)
print("Sorted list:  ", sorted_numbers)
