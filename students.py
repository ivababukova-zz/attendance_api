from student import Student


class Students:
    def __init__(self):
        self.students = [
            Student(
                student_id="1234",
                full_name="JohnSmith",
                courses=["ADS2", "Databases", "Maths 2E"],
            ),
            Student(
                student_id="4567",
                full_name="Adam Kurkiewicz",
                courses=["Abstract Algebra", "Chemistry 2D", "Systems 2", "Algorithms 3"],
            ),
            Student(
                student_id="8910",
                full_name="Marcell Pek",
                courses=["Physics 2A", "Maths 2E", "Algorithms 3", "Databases"],
            ),
            Student(
                student_id="1112",
                full_name="Iva Babukova",
                courses=["ADS2", "Databases", "Maths 2E", "Systems 2"],
            )
        ]

    def add_student(self, student_id, full_name, courses, attendance=None):
        s = Student(student_id, full_name, courses, attendance)
        self.students.append(s)

    def get_student_by_id(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s, dict(
                    student_id=s.student_id,
                    full_name=s.full_name,
                    courses=s.courses,
                    attendance=s.attendance
                )
            return None, {"message": "student not found"}

    def get_student_by_name(self, full_name):
        for s in self.students:
            if s.full_name == full_name:
                return s, dict(
                    student_id=s.student_id,
                    full_name=s.full_name,
                    courses=s.courses,
                    attendance=s.attendance
                )
        return None, {"message": "student not found"}

    def get_attendance_for_student(self, student_name, courses=None):
        s = self.get_student_by_name(student_name)
        return s.get_attendance_for_course(courses)


