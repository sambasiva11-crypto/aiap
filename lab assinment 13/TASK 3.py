class Student:
    """
    Represents a student with name, age, and subject marks.
    Provides utilities to display details and calculate total marks.
    """
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks  # List of marks

    def show_details(self):
        print(f"Name: {self.name} | Age: {self.age}")

    def total_marks(self):
        return sum(self.marks)
