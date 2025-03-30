class Student:
    def __init__(self, name = None, age = None, id = None, courses = None):
        self.name = name
        self.id = id
        self.age = age
        if not courses:
            self.courses = []
        else:
            self.courses = courses


    grade_points = {
        "A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0}

    @classmethod
    def calculate_grades(cls, grades):
        total = 0
        if not grades:
            return total
        else:
            for grade in grades:
                total = total + cls.grade_points[grade]
            return total / len(grades)


    def setter(self):
        return self.name, self.age, self.id, self.courses

    def __str__(self):
        return f"{self.name} is {self.age} years old and had taken {self.courses} courses"


class Graduate_Student(Student):
    def __init__(self, name = None, age = None, id = None, courses = None, thesis = None):
        super().__init__(name, id, age, courses)
        self.thesis = thesis

    def __str__(self):
        return f"{super().__str__()} and is working on {self.thesis} topic"



# Test code for Student and Graduate_Student classes

# Test Case 1: Basic Student with no parameters
print("Test Case 1: Empty Student")
student1 = Student()
print(student1)
print(f"GPA: {Student.calculate_grades([])}")  # Empty grades list
print()

# Test Case 2: Student with all parameters
print("Test Case 2: Student with all parameters")
student2 = Student("John Doe", 20, "S123", ["Math", "Physics"])
print(student2)
grades2 = ["A", "B+", "A-"]
print(f"GPA: {Student.calculate_grades(grades2)}")
print()


# Test Case 3: Testing setter method
print("Test Case 3: Testing setter method")
student4 = Student("Bob Wilson", 21, "S789", ["Chemistry"])
name, age, id_num, courses = student4.setter()
print(f"Name: {name}, Age: {age}, ID: {id_num}, Courses: {courses}")
grades4 = ["A+", "A", "B"]
print(f"GPA: {Student.calculate_grades(grades4)}")
print()

# Test Case 4: Basic Graduate Student
print("Test Case 4: Basic Graduate Student")
grad1 = Graduate_Student("Alice Brown", 25, "G123", ["Advanced Math"], "Quantum Physics")
print(grad1)
grades5 = ["A", "A-", "B+"]
print(f"GPA: {Graduate_Student.calculate_grades(grades5)}")  # Using inherited method
print()
