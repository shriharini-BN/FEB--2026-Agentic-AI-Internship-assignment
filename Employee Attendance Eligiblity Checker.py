def attendance_check(attendance_list):
    present = 0
    for day in attendance_list:
        if day == "P":
            present += 1
    percentage = (present / len(attendance_list)) * 100
    if percentage >= 75:
        return "Eligible"
    else:
        return "Not Eligible"
attendance_list = ["P", "P", "A", "P", "P", "A", "P"]
print(attendance_check(attendance_list))