def attendance_percentage(days_present, total_days):
    percentage = (days_present/total_days)*100
    per = round(percentage,2)
    return per

if __name__ == "__main__":
    data = attendance_percentage(20, 30)
    print(data)
