# ...existing code...
def cm_to_inches(cm):
    """
    Convert centimeters to inches.
    1 inch = 2.54 cm
    Args:
        cm (float): length in centimeters
    Returns:
        float: length in inches
    """
    return cm / 2.54


if __name__ == "__main__":
    s = input("Enter centimeters (single value or comma-separated list): ").strip()
    if not s:
        print("No input provided.")
    else:
        try:
            parts = [p.strip() for p in s.split(",")]
            values = [float(p) for p in parts]
        except ValueError:
            print("Invalid input. Enter numeric values only (e.g. 10 or 10, 25.4).")
        else:
            for cm in values:
                inches = cm_to_inches(cm)
                print(f"{cm} cm = {inches:.4f} in")
# ...existing code...