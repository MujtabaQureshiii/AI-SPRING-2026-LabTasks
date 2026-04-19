class Staff:
    def __init__(self, name, staff_id, department):
        self.name = name
        self.staff_id = staff_id
        self.department = department

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Department: {self.department}")

class Teacher(Staff):
    def __init__(self, name, staff_id, department, subjects, salary):
        super().__init__(name, staff_id, department)
        self.subjects = subjects
        self.salary = salary

    def conduct_class(self):
        print(f"{self.name} is conducting classes of {', '.join(self.subjects)}.")

    def show_details(self):
        super().show_details()
        print(f"Subjects: {', '.join(self.subjects)}")
        print(f"Salary: {self.salary}")

class AdminStaff(Staff):
    def __init__(self, name, staff_id, department, designation, duty_hours):
        super().__init__(name, staff_id, department)
        self.designation = designation
        self.duty_hours = duty_hours

    def handle_office_work(self):
        print(f"{self.name} is handling office work as {self.designation}.")

    def show_details(self):
        super().show_details()
        print(f"Designation: {self.designation}")
        print(f"Duty Hours: {self.duty_hours}")

class ResearchAssistant(Staff):
    def __init__(self, name, staff_id, department, research_area, stipend):
        super().__init__(name, staff_id, department)
        self.research_area = research_area
        self.stipend = stipend

    def perform_research(self):
        print(f"{self.name} is working on research area: {self.research_area}.")

    def show_details(self):
        super().show_details()
        print(f"Research Area: {self.research_area}")
        print(f"Stipend: {self.stipend}")

teacher = Teacher("Dr. Ahmed Khan", "T110", "Computer Science", ["AI", "OOP"], 150000)
admin = AdminStaff("Ms. Ayesha Malik", "A220", "Administration", "Office Supervisor", 8)
researcher = ResearchAssistant("Muhammad Hassan", "R330", "Computer Science", "Data Science", 50000)

teacher.conduct_class()
admin.handle_office_work()
researcher.perform_research()

print()

teacher.show_details()
print()
admin.show_details()
print()
researcher.show_details()
