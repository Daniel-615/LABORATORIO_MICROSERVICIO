from src.routes.certificado_factura.certificado_factura_routes import CertificadoFacturaRoutes as CFR
from src.controllers.certificado_factura.certificado_factura_controllers import CertificadoFacturaControllers as CFC
from src.services.certificado_factura.certificado_factura_services import CertificadoFacturaServices as CFS
class AppInitializer:
    def __init__(self,app,db,models):
        self.app=app
        self.services(db,models)
        self.controllers()
        self.routes()
    
    #Getters and setters
    def getServices(self):
        return self.certificado_factura_services
    def getControllers(self):
        return self.certificado_factura_controllers
    def getRoutes(self):
        return self.certificado_factura_routes
    def services(self,db,models):
        self.certificado_factura_services=CFS(db,models)
    def controllers(self):
        self.certificado_factura_controllers=CFC(self.getServices())
    def routes(self):
        self.certificado_factura_routes=CFR(self.app,self)