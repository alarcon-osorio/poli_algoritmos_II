# app.py

from flask import Flask
from config import db, DATABASE_URI
from routes.coursesRoutes import course_bp
from routes.studentsRouter import student_bp
from flask_cors import CORS  # Importamos flask_cors
from flask_migrate import Migrate

app = Flask(__name__)

# Configurar la URI de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)
migrate = Migrate(app, db)  # Inicializa Flask-Migrate con la aplicación y la base de datos

# Registrar los Blueprints de las rutas

#app.register_blueprint(student_bp)
#app.register_blueprint(course_bp)

app.register_blueprint(course_bp, url_prefix='/api/v1.0')
app.register_blueprint(student_bp, url_prefix='/api/v1.0')

# Crear las tablas si no existen
with app.app_context():
    db.create_all()

# Habilitar CORS en toda la aplicación
CORS(app)  # Esto habilita CORS para todas las rutas y todos los orígenes

# Si deseas habilitar CORS solo para ciertas rutas, usa:
# CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(debug=True)
