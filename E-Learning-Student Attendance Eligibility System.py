def attendance_check(attendance):
    total_classes = len(attendance)
    present = 0
    for day in attendance:
        if day == 1:
            present += 1
    percentage = (present / total_classes) * 100
    if percentage >= 75:
        status = "Eligible"
    else:
        status = "Not Eligible"
    print("Attendance Percentage:", percentage)
    print("Exam Eligibility:", status)
attendance_check([1,1,1,0,1,1,1,1])