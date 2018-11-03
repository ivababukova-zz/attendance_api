from students import Students

from flask import Flask, jsonify
app = Flask(__name__)

all_students = Students()


@app.route('/students', methods=['GET'])
def get_students():
    return "Hello world"
    # return all_students


@app.route('/student/<id>')
def get_student_by_name(id):
    _, data = all_students.get_student_by_id(id)
    return jsonify(data)


@app.route('/attendance/<id>')
def get_student_attendance(id):
    student, _ = all_students.get_student_by_id(id)
    return jsonify(student.get_attendance_for_courses())

#
# @app.route('/attendance/<student_name>/<courses>')
# def get_student_attendance_for_course(student_name, courses):
#     student = all_students.get_student_by_name(student_name)
#     return jsonify(student.get_attendance_for_courses(courses))


if __name__ == '__main__':
    app.run(debug=True)