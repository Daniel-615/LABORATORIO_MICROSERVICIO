
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env', override=True)
class Connection:
    def __init__(self):
       self.host = os.getenv("DB_HOST", "localhost")
       self.user = os.getenv("DB_USER", "root")
       self.password = os.getenv("DB_PASSWORD", "angel1234")
       self.database = os.getenv("DB_NAME", "certificado_factura")
       self.port = int(os.getenv("DB_PORT", 3306))


    def getHost(self):
        return self.host
    def getUser(self):
        return self.user
    def getPassword(self):
        return self.password
    def getDatabase(self):
        return self.database
    def getPort(self):
        return self.port
    def connect(self):
        try:
            connection= f"mysql+mysqlconnector://{self.getUser()}:{self.getPassword()}@{self.getHost()}:{self.getPort()}/{self.getDatabase()}"
            return connection
        except Exception as e:
            print(f"Error al parsear la ruta: {e}")

