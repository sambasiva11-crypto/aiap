def count_lines(file_path):
    """
    Read a text file and return the number of lines.
    Args:
        file_path (str): Path to the text file
    Returns:
        int: Number of lines in the file
    Raises:
        FileNotFoundError: If the file does not exist
        IOError: If there's an error reading the file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return -1
    except IOError as e:
        print(f"Error reading file: {e}")
        return -1
if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ").strip()
    
    if not file_path:
        print("No file path provided.")
    else:
        line_count = count_lines(file_path)
        if line_count >= 0:
            print(f"The file '{file_path}' contains {line_count} line(s).")