import csv
import statistics

def analyze_csv():
    """Reads a CSV file and calculates mean, min, max for a selected column."""
    # Get file path from user
    file_path = input("Enter the CSV file path: ")
    try:
        # Read the CSV file
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames
            if not headers:
                print("Error: CSV file is empty or has no headers.")
                return
                print(f"\nAvailable columns: {', '.join(headers)}")
             # Get column name from user
            column_name = input("Enter the column name to analyze: ")
            if column_name not in headers:
                print(f"Error: '{column_name}' not found in CSV headers.")
                return
            # Extract numeric values from the selected column
            values = []
            for row in reader:
                try:
                    value = float(row[column_name])
                    values.append(value)
                except ValueError:
                    print(f"Warning: Skipping non-numeric value '{row[column_name]}'")
            if not values:
                print("Error: No numeric values found in the selected column.")
                return
            # Calculate statistics
            mean_val = statistics.mean(values)
            min_val = min(values)
            max_val = max(values)
            # Display results
            print(f"\n--- Statistics for Column: {column_name} ---")
            print(f"Mean: {mean_val:.2f}")
            print(f"Minimum: {min_val:.2f}")
            print(f"Maximum: {max_val:.2f}")
            print(f"Count: {len(values)}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")
# Main execution
if __name__ == "__main__":
    analyze_csv()