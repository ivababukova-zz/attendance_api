from students import Students

from flask import Flask, jsonify, send_from_directory
app = Flask(__name__)

all_students = Students()


@app.route('/')
def get_index():
    return send_from_directory("mocks/", "dashboard.html")


@app.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory("mocks/assets/", path)


@app.route('/students')
def get_students():
    resp = []
    for s in all_students.students:
        _, student_data = all_students.get_student_by_id(s.student_id)
        resp.append(student_data)
    return jsonify({"students": resp})


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


@app.route('/courses')
def get_all_courses():
    return jsonify({
        "courses": all_students.get_all_courses()
    })


@app.route("/courses/attendance/<course>")
def get_course_attendance(course):
    return jsonify(all_students.get_course_attendance(course))


@app.route('/courses/<id>')
def get_student_courses(id):
    student, _ = all_students.get_student_by_id(id)
    return jsonify({
        "student_name": student.full_name,
        "courses": student.courses
    })


if __name__ == '__main__':
    app.run(debug=True)
