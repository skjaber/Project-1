class student:
    def __init__(self, name, id, dept):
        self.name = name
        self.id = id
        self.dept = dept

    def myfunc(self):
        return f"NAME = {self.name}, ID = {self.id}, Dept. = {self.dept}"

studentslist = [
    student("Md. Reahoon Zannah", 223002038, "CSE"),
    student("Sara Ali Khan", 223002039, "CSE"),
    student("Ahmed Rafi", 223002040, "CSE"),
    student("Sofia Ahmed", 223002041, "CSE"),
    student("Zeeshan Ali", 223002042, "ECE"),
    student("Tariq Jameel", 223002043, "ECE"),
    student("Ayesha Ali", 223002044, "BBA"),
    student("Imran Khan", 223002045, "BBA"),
    student("Fatima Zahra", 223002046, "Physics"),
    student("Bilal Yousuf", 223002047, "Physics"),
    student("Nadia Hussain", 223002048, "Maths"),
    student("Khalid Mehmood", 223002049, "Maths")
]

for student_instance in studentslist:
    print(student_instance.myfunc())

