def evaluate_performance(grade_percentage, attendance_percentage, min_attendance=75):

    # Weightages: 70% for grades, 30% for attendance
    weighted_score = (0.7 * grade_percentage) + (0.3 * attendance_percentage)
    
    # Check if attendance meets minimum requirement
    attendance_status = attendance_percentage >= min_attendance
    
    if not attendance_status:
        return "Unsatisfactory (Low Attendance)"
    
    if weighted_score >= 90:
        return "Excellent"
    elif weighted_score >= 80:
        return "Good"
    elif weighted_score >= 70:
        return "Satisfactory"
    elif weighted_score >= 60:
        return "Needs Improvement"
    else:
        return "Unsatisfactory"
    
if __name__=="__main__":
    # Test the function 
    grade_percentage = 75
    attendance_percentage = 80
    min_attendance = 75
    result = evaluate_performance(grade_percentage, attendance_percentage, min_attendance)
    print(result) 