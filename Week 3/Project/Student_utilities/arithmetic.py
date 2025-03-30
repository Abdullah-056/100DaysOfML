def cal_percentage(subject_marks):
    percentage = sum(subject_marks)/len(subject_marks)
    return percentage

def grade(subject_marks):
    grade = {"A+":90, "A":85, "B+":80, "B-":75, "C+":70, "C-":65,
              "D+":60, "D-":55, "F":50}
    percentage = sum(subject_marks)/len(subject_marks)
    graden = None 
    val = round(percentage/5)*5
    for key, value in grade.items():
        if val >= value:
            graden = key 
            break

    if(percentage <= 50):
        graden = "F"
    return graden

if __name__ == "__main__":
    per  = cal_percentage([90, 85, 80, 75, 70, 65, 60, 55, 50, 100])
    print(per)