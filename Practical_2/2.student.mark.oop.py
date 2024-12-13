class Person:
    def __init__(self, person_id, name, dob):
        self._id = person_id
        self._name = name
        self._dob = dob

    def get_info(self):
        return self._id, self._name, self._dob

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, DoB: {self._dob}"

class Student(Person):
    def __init__(self, student_id, name, dob):
        super().__init__(student_id, name, dob)

class Course:
    def __init__(self, course_id, name):
        self._id = course_id
        self._name = name
        self._marks = {}

    def input_marks(self, students):
        print(f"Enter marks for course: {self._name} (ID: {self._id})")
        for student in students:
            student_id, student_name, _ = student.get_info()
            mark = float(input(f"Enter mark for {student_name} (ID: {student_id}): "))
            self._marks[student_id] = mark

    def show_marks(self):
        print(f"Marks for course: {self._name} (ID: {self._id})")
        for student_id, mark in self._marks.items():
            print(f"Student ID: {student_id}, Mark: {mark}")

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}"

class StudentMarkManagement:
    def __init__(self):
        self._students = []
        self._courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (DD/MM/YYYY): ")
            self._students.append(Student(student_id, name, dob))

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self._courses.append(Course(course_id, name))

    def list_students(self):
        print("Students:")
        for student in self._students:
            print(student)

    def list_courses(self):
        print("Courses:")
        for course in self._courses:
            print(course)

    def input_marks_for_course(self):
        course_id = input("Enter course ID to input marks: ")
        course = next((c for c in self._courses if c._id == course_id), None)
        if course:
            course.input_marks(self._students)
        else:
            print("Course not found.")

    def show_marks_for_course(self):
        course_id = input("Enter course ID to view marks: ")
        course = next((c for c in self._courses if c._id == course_id), None)
        if course:
            course.show_marks()
        else:
            print("Course not found.")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. List students")
            print("2. List courses")
            print("3. Input marks for a course")
            print("4. Show marks for a course")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.list_students()
            elif choice == "2":
                self.list_courses()
            elif choice == "3":
                self.input_marks_for_course()
            elif choice == "4":
                self.show_marks_for_course()
            elif choice == "5":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "_main_":
    smm = StudentMarkManagement()
    smm.input_students()
    smm.input_courses()
    smm.menu()
