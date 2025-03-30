
try:
    with open("student_records.txt", "r") as file:
        line = file.readlines()

    
    with open("student_records_by_code.txt", "w") as file:
        for i in line:
            file.write(i)

    stud = 0
    for i in line:
        if("Student" in i):
            stud = stud + 1
except FileNotFoundError:
    print("Fle is not found or path is incorrect")
except IOError:
    print("Could not read file:", file)
except Exception as e:
    print("An error occurred:", e)

print(f"Total number of students: {stud}")
# In txt file there is Studend 1, Student 2 Written , by calculating the number of students in the file, we can find the no of studens
# Otherewise, we have to store student data in a single line and by calculating no. of lines we can calculate no. of students