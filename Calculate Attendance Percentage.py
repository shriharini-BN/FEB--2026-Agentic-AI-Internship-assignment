attendance = ["P", "P", "A", "P", "P"]
present_count = attendance.count("P")
total_days = len(attendance)
percentage = (present_count / total_days) * 100
print("Attendance Percentage:", percentage)