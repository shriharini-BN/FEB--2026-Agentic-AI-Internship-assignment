def student_result(marks):
    total = 0
    for mark in marks:
        total += mark
    average = total / len(marks)
    if average >= 50:
        return "Pass"
    else:
        return "Fail"
marks_list = [60, 70, 40, 50]
print(student_result(marks_list))