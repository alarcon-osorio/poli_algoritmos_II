# models/student_course_model.py
from config import db

# Definimos la tabla intermedia
class StudentCourse(db.Model):
    __tablename__ = 'student_course'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

    student = db.relationship('Students', backref='student_courses')  # backref único
    course = db.relationship('Courses', backref='student_courses')    # backref único
