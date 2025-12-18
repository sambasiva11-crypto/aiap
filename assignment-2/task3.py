# ...existing code...
import math
def _positive_float(prompt: str) -> float:
    while True:
        try:
            v = float(input(prompt))
            if v > 0:
                return v
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")
def calculate_area():
    """Ask user for a shape and required dimensions, then print the area."""
    shapes = {
        "1": "Circle",
        "2": "Rectangle",
        "3": "Square",
        "4": "Triangle",
        "5": "Trapezoid",
        "6": "Ellipse",
        "7": "Parallelogram",
    }
    print("Choose a shape:")
    for k, name in shapes.items():
        print(f"{k}. {name}")
    choice = input("Enter choice (1-7): ").strip()
    if choice == "1":  # Circle
        r = _positive_float("Radius: ")
        area = math.pi * r * r
    elif choice == "2":  # Rectangle
        l = _positive_float("Length: ")
        w = _positive_float("Width: ")
        area = l * w
    elif choice == "3":  # Square
        s = _positive_float("Side: ")
        area = s * s
    elif choice == "4":  # Triangle
        b = _positive_float("Base: ")
        h = _positive_float("Height: ")
        area = 0.5 * b * h
    elif choice == "5":  # Trapezoid
        a = _positive_float("Base a: ")
        b = _positive_float("Base b: ")
        h = _positive_float("Height: ")
        area = 0.5 * (a + b) * h
    elif choice == "6":  # Ellipse
        a = _positive_float("Semi-major axis a: ")
        b = _positive_float("Semi-minor axis b: ")
        area = math.pi * a * b
    elif choice == "7":  # Parallelogram
        base = _positive_float("Base: ")
        height = _positive_float("Height: ")
        area = base * height
    else:
        print("Invalid choice.")
        return
    print(f"Area: {area:.4f}")
if __name__ == "__main__":
    calculate_area()
# ...existing code...