class Student:
    def __init__(self, roll_number, name, marks={}):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def add_marks(self, subject, score):
        self.marks[subject] = score

    def get_average_score(self):
        total_score = sum(self.marks.values())
        return total_score / len(self.marks)

    def display_student_info(self):
        print(f"Roll Number: {self.roll_number}")
        print(f"Name: {self.name}")
        if self.marks:
            print("Marks:")
            for subject, score in self.marks.items():
                print(f"{subject}: {score}")
            print(f"Average Score: {self.get_average_score()}")
        else:
            print("No marks available for this student.")

class MenuDrivenProgram:
    def __init__(self):
        self.students = {}

    def add_student(self):
        roll_number = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        self.students[roll_number] = Student(roll_number, name)
        print(f"Student {name} with Roll Number {roll_number} added.")

    def add_marks(self):
        roll_number = input("Enter Roll Number of the student: ")
        if roll_number in self.students:
            student = self.students[roll_number]
            subject = input("Enter Subject: ")
            score = float(input("Enter Score: "))
            student.add_marks(subject, score)
            print(f"{subject} score added for {student.name}")
        else:
            print("Student not found.")

    def display_student_info(self):
        roll_number = input("Enter Roll Number of the student: ")
        if roll_number in self.students:
            student = self.students[roll_number]
            student.display_student_info()
        else:
            print("Student not found.")

    def show_menu(self):
        while True:
            print("\nMenu:")
            print("1. Add Student")
            print("2. Add Marks")
            print("3. Display Student Info")
            print("4. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_marks()
            elif choice == '3':
                self.display_student_info()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    program = MenuDrivenProgram()
    program.show_menu()
