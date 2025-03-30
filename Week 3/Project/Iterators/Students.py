# iterate through enroleld students

class StudentLists:
    def __init__(self, students):
        self.students = students
        self.index = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            if(self.index >= len(self.students)):
                raise StopIteration
            student = self.students[self.index]
            self.index += 1
            return student
        except StopIteration:
            print("End of the list")


import random
def attendence_studence(student):
    for student in students:
        yield(student, random.choice(["Present", "Absent" ]))

def random_marks_generator(students):
    for student in students:
        yield (student, random.randint(50, 100))


if __name__ == "__main__":
    students = ["John", "Jane", "Jack", "Jill"]
    print("Students Enrolled:")
    names = StudentLists(students)
    print(next(names))
    print(next(names))
    print("000000000000000000000000000000000000000")
    print("Attendence:")
    attendence = attendence_studence(students)
    print(next(attendence))
    print(next(attendence))
    print("000000000000000000000000000000000000000")
    print("Attendence:")
    marks =  random_marks_generator(students)
    print(next(marks))
    print(next(marks))
    


