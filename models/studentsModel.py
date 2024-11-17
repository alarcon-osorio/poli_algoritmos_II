from config import db
from models.courseStudentModel import StudentCourse  # Importa la tabla intermedia

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cc = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Relación muchos a muchos con Cursos a través de la tabla intermedia
    courses = db.relationship('Courses', secondary='student_course', backref='students_list')

    def to_dict(self):
        # Evitamos la recursión: solo mostramos los IDs de los cursos y no sus objetos completos
        return {
            'id': self.id,
            'cc': self.cc,
            'name': self.name,
            'email': self.email,
            'courses': [course.id for course in self.courses]  # Solo devolvemos los IDs de los cursos
        }
