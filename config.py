from flask_sqlalchemy import SQLAlchemy

# Configuración de la base de datos
DATABASE_URI = 'mysql+pymysql://admin:admin@localhost:3306/usuarios'
db = SQLAlchemy()
