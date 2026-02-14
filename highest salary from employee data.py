employees = {"Ravi": 75000, "Anita": 68000, "Kiran": 72000}
highest_employee = max(employees, key=employees.get)
print("Highest Salary:", highest_employee, "-", employees[highest_employee])