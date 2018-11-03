import random

# search for student
# attendance data

WEEKS_PER_SEMESTER = 12


class Student:
    def __init__(self, student_id, full_name, courses, attendance=None):
        self.student_id = student_id
        self.full_name = full_name
        self.courses = courses
        if not attendance:
            self.attendance = {}
            self.init_attendance()
        else:
            self.attendance = attendance

    def _get_random_list(self, n):
        my_list = []
        for _ in range(n):
            k = random.randint(0, 1)
            my_list.append(k)
        return my_list

    def init_attendance(self):
        for course in self.courses:
            self.attendance[course] = self._get_random_list(WEEKS_PER_SEMESTER)

    def record_attendance(self, course_name, week_no):
        self.attendance[course_name][week_no-1] = 1

    def unrecord_attendance(self, course_name, week_no):
        self.attendance[course_name][week_no-1] = 0

    def get_attendance_for_courses(self, course_names=None):
        attendance = {}
        if not course_names:
            return self.attendance

        for c in course_names:
            if self.attendance.get(str(c)):
                attendance[c] = self.attendance[c]
                print(attendance[c])
        print(attendance)
        return attendance
