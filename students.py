from student import Student


class Students:
    def __init__(self):
        self.students = [
            Student(
                student_id="1234",
                full_name="John Smith",
                courses=["ADS2", "Databases", "Maths"],
            ),
            Student(
                student_id="4567",
                full_name="Adam Kurkiewicz",
                courses=["AbstractAlgebra", "Chemistry", "Systems2", "Algorithms3"],
            ),
            Student(
                student_id="8910",
                full_name="Marcell Pek",
                courses=["Physics", "Maths2E", "Algorithms3", "Databases"],
            ),
            Student(
                student_id="1112",
                full_name="Iva Babukova",
                courses=["ADS2", "Databases", "Maths", "Systems2"],
            ),
            Student(
                student_id="0000",
                full_name="Balint Zsilavecz",
                courses=["ADS2", "Javascript4", "Analytics", "Entrepreneurship"],
            ),
            Student(
                student_id="1111",
                full_name="Ross Imlach",
                courses=["InteractiveSystems", "Modeling", "Analytics", "Entrepreneurship"],
            ),
            Student(
                student_id="2222",
                full_name="Andrew Gardner",
                courses=["AbstractAlgebra", "Maths", "Algorithms3", "Databases"],
            ),
            Student(
                student_id="3333",
                full_name="Grant Henderson",
                courses=["ADS2", "Databases", "Chemistry", "Systems2"],
            ),
            Student(
                student_id="4444",
                full_name="Jim Cockburn",
                courses=["ADS2", "Databases", "Physics", "InteractiveSystems", "Algorithms3", "Maths"],
            ),
            Student(
                student_id="5555",
                full_name="Adam Kurkiewicz",
                courses=["Maths", "Chemistry", "Systems2", "Maths"],
            ),
            Student(
                student_id="6666",
                full_name="Stuart Davidson",
                courses=["Modelling", "AbstractAlgebra", "Algorithms3", "Databases"],
            ),
            Student(
                student_id="7777",
                full_name="Guy Templeton",
                courses=["ADS2", "Databases", "Maths", "Systems2", "Chemistry", "Electronics"],
            ),
            Student(
                student_id="8888",
                full_name="Kenny Smith",
                courses=["ADS2", "Databases", "Maths", "Systems2"],
            ),
            Student(
                student_id="9999",
                full_name="Rosalyn Tailor",
                courses=["AbstractAlgebra", "Chemistry", "Systems2", "Algorithms3"],
            ),
            Student(
                student_id="1010",
                full_name="Graham Martin",
                courses=["Physics", "Maths", "Algorithms3", "Databases"],
            ),
            Student(
                student_id="1212",
                full_name="Colin Millar",
                courses=["ADS2", "Databases", "Maths", "Systems2", "Algorithms3", "Electronics", "Physics"],
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
        s, _ = self.get_student_by_name(student_name)
        return s.get_attendance_for_courses(courses)
