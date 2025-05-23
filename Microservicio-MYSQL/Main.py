from flask import Flask
from src.connection.db_connection import Connection
from src.models.models import Models
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from src.config.app_initializer import AppInitializer
class Main:
    def __init__(self):
        self.app = Flask(__name__)

        self.connection = Connection()
        try:
            uri=self.connection.connect()
            if not uri:
                raise ValueError("No se pudo encontrar la URI de la base de datos.")
            self.app.config['SQLALCHEMY_DATABASE_URI'] = uri  
        except Exception as e:
            print(f"Error al conectarse: {e}")
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
        
        self.db = SQLAlchemy(self.getApp())
        self.models = Models(self.db)
        with self.app.app_context():
             self.db.create_all()
        self.migrate = Migrate(self.getApp(), self.db)  # Migraciones de la base de datos
        self.app_initializer = AppInitializer(self.getApp(),self.db,self.models)  # Inicializador de la aplicación
    def startApp(self):
        self.app.run(debug=True,host="0.0.0.0",port=3000)
    def getApp(self):
        return self.app