class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department
    def display_id_card(self):
        print("Employee ID Card")
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Department:", self.department)
emp = Employee("Rahul", "EMP102", "IT")
emp.display_id_card()