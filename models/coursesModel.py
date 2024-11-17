from config import db
from models.courseStudentModel import StudentCourse  # Importa la tabla intermedia

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    # Relación muchos a muchos con Estudiantes a través de la tabla intermedia
    students = db.relationship('Students', secondary='student_course', backref='courses_list')

    def to_dict(self):
        # Evitamos la recursión: solo mostramos los IDs de los estudiantes y no sus objetos completos
        return {
            'id': self.id,
            'name': self.name,
            'students': [student.id for student in self.students]  # Solo devolvemos los IDs de los estudiantes
        }
