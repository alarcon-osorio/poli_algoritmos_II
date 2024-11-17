# routes/user_routes.py

from flask import Blueprint, request, jsonify
from models.coursesModel import Courses
from models.studentsModel import Students
from config import db

course_bp = Blueprint('course_bp', __name__)

# GET - Obtener todos los cursos con sus estudiantes
@course_bp.route('/courses_with_students', methods=['GET'])
def get_courses_with_students():
    courses = Courses.query.all()
    return jsonify([course.to_dict() for course in courses])

# GET - Obtener todos los cursos
@course_bp.route('/courses', methods=['GET'])
def get_courses():
    courses = Courses.query.all()
    return jsonify([course.to_dict() for course in courses])


# POST - Crear un nuevo curso y asignar estudiantes
@course_bp.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    new_course = Courses(name=data['name'])

    # Si se proporciona una lista de student_ids, asignarlos al curso
    if 'student_ids' in data:
        students = Students.query.filter(Students.id.in_(data['student_ids'])).all()
        new_course.students.extend(students)

    db.session.add(new_course)
    db.session.commit()
    return jsonify(new_course.to_dict()), 201

# PUT - Actualizar un curso existente
@course_bp.route('/courses/<int:id>', methods=['PUT'])
def update_course(id):
    course = Courses.query.get_or_404(id)
    data = request.get_json()
    course.name = data['name']
    db.session.commit()
    return jsonify(course.to_dict())

# DELETE - Eliminar un curso
@course_bp.route('/courses/<int:id>', methods=['DELETE'])
def delete_course(id):
    curse = Courses.query.get_or_404(id)
    db.session.delete(curse)
    db.session.commit()
    return jsonify({'message': 'Curso eliminado correctamente'})
