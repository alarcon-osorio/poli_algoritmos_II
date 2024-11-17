# routes/user_routes.py

from flask import Blueprint, request, jsonify
from models.coursesModel import Courses
from models.studentsModel import Students
from config import db

student_bp = Blueprint('student_bp', __name__)

# GET - Obtener todos los estudiantes con sus cursos
@student_bp.route('/students_with_courses', methods=['GET'])
def get_students_with_courses():
    students = Students.query.all()
    return jsonify([student.to_dict() for student in students])

# GET - Obtener todos los usuarios
@student_bp.route('/students', methods=['GET'])
def get_students():
    students = Students.query.all()
    return jsonify([student.to_dict() for student in students])


# POST - Crear un nuevo estudiante y asignar cursos
@student_bp.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = Students(cc=data['cc'], name=data['name'], email=data['email'])

    # Si se proporciona una lista de course_ids, asignarlos al estudiante
    if 'course_ids' in data:
        courses = Courses.query.filter(Courses.id.in_(data['course_ids'])).all()
        new_student.courses.extend(courses)

    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.to_dict()), 201

# PUT - Actualizar un usuario existente
@student_bp.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    user = Students.query.get_or_404(id)
    data = request.get_json()
    user.cc = data['cc']
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify(user.to_dict())

# DELETE - Eliminar un usuario
@student_bp.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    user = Students.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Usuario eliminado correctamente'})
