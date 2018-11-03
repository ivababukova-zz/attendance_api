from students import Students

from flask import Flask, jsonify
app = Flask(__name__)

all_students = Students()


@app.route('/students')
def get_students():
    resp = []
    for s in all_students.students:
        _, student_data = all_students.get_student_by_id(s.student_id)
        resp.append(student_data)
    return jsonify({"resp": resp})


@app.route('/student/<id>')
def get_student_by_name(id):
    _, data = all_students.get_student_by_id(id)
    return jsonify(data)


@app.route('/attendance/<id>')
def get_student_attendance(id):
    student, _ = all_students.get_student_by_id(id)
    return jsonify(student.get_attendance_for_courses())


@app.route('/attendance/<id>/<courses>')
def get_student_attendance_for_course(id, courses):
    if courses:
        courses = courses.split(",")
    student, _ = all_students.get_student_by_id(id)
    return jsonify(student.get_attendance_for_courses(courses))


@app.route('/courses/<id>')
def get_courses(id):
    student, _ = all_students.get_student_by_id(id)
    return jsonify({
        "student_name": student.full_name,
        "courses": student.courses
    })


if __name__ == '__main__':
    app.run(debug=True)
