# 09 - Student Management System using OOP + JSON.
import json
import os

FILE = "students.json"

class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course
        }

    def display(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Course: {self.course}")

class StudentManagementSystem:
    def __init__(self):
        self.students = self.load_students()

    def load_students(self):
        if not os.path.exists(FILE):
            return []
        try:
            with open(FILE, "r") as f:
                data = json.load(f)
                return [Student(s['id'], s['name'], s['age'], s['course']) for s in data]
        except:
            return []

    def save_students(self):
        with open(FILE, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def add_student(self):
        sid = input("Enter ID: ").strip()
        # check duplicate
        if any(s.student_id == sid for s in self.students):
            print("ID already exists!")
            return
        name = input("Enter Name: ").strip()
        age = input("Enter Age: ").strip()
        course = input("Enter Course: ").strip()
        
        self.students.append(Student(sid, name, age, course))
        self.save_students()
        print("Student added!")

    def view_all(self):
        if not self.students:
            print("No students found!")
            return
        print("\n--- All Students ---")
        for s in self.students:
            s.display()

    def search_student(self):
        sid = input("Enter ID to search: ").strip()
        for s in self.students:
            if s.student_id == sid:
                print("Found:")
                s.display()
                return
        print("Not found!")

    def delete_student(self):
        sid = input("Enter ID to delete: ").strip()
        for s in self.students:
            if s.student_id == sid:
                self.students.remove(s)
                self.save_students()
                print("Deleted!")
                return
        print("Not found!")

    def update_student(self):
        sid = input("Enter ID to update: ").strip()
        for s in self.students:
            if s.student_id == sid:
                s.name = input(f"New Name ({s.name}): ") or s.name
                s.age = input(f"New Age ({s.age}): ") or s.age
                s.course = input(f"New Course ({s.course}): ") or s.course
                self.save_students()
                print("Updated!")
                return
        print("Not found!")

# MAIN MENU - this is OOP in action
sms = StudentManagementSystem()

while True:
    print("\n--- Student Management System [OOP] ---")
    print("1. Add Student")
    print("2. View All")
    print("3. Search")
    print("4. Delete")
    print("5. Update")
    print("6. Exit")
    
    ch = input("Choose 1-6: ").strip()

    if ch == '1': sms.add_student()
    elif ch == '2': sms.view_all()
    elif ch == '3': sms.search_student()
    elif ch == '4': sms.delete_student()
    elif ch == '5': sms.update_student()
    elif ch == '6': break
    else: print("Invalid!")
