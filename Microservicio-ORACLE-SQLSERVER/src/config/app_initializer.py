from src.services.sql_server.facturacion_services import FacturacionServices as F_S
from src.services.sql_server.vendedor_services import VendedorServices as V_S
from src.services.oracle.factura_detalle_services import FacturaDetalleServices as FD_S
from src.services.oracle.producto_services import ProductoServices as P_S

from src.controllers.sql_server.facturacion_controller import FacturacionController as F_C
from src.controllers.sql_server.vendedor_controller import VendedorController as V_C
from src.controllers.oracle.factura_detalle_controller import FacturaDetalleController as FD_C
from src.controllers.oracle.producto_controller import ProductoController as P_C

from src.routes.sql_server.facturacion_routes import FacturacionRoutes as F_R
from src.routes.sql_server.vendedor_routes import VendedorRoutes as V_R
from src.routes.oracle.factura_detalle_routes import FacturaDetalleRoutes as FD_R
from src.routes.oracle.producto_routes import ProductoRoutes as P_R

class AppInitializer:
    def __init__(self,app,db,models):
        self.app=app
        self.models=models
        """
        la instancia bd tiene tanto 
        el motor sql server y 
        el motor oracle para diferenciarlos 
        es por medio del key_bind este solo se usa para oracle, 
        esta en default para sql server
        """
        self.services_sql_server(db,models)
        self.services_oracle(db,models)
        self.controllers_oracle()
        self.controllers_sql_server()
        self.routes_oracle()
        self.routes_sql_server()
    
    #getters 
    def getModels(self):
        return self.models
    def getServicesSqlServer(self):
        return self.facturacion_services,self.vendedor_services
    def getServicesOracle(self):
        return self.producto,self.factura_detalle
    def getControllersFacturacion(self):
        return self.facturacion_controller
    def getControllersVendedor(self):
        return self.vendedor_controller
    def getControllersProducto(self):
        return self.producto_controller
    def getControllersFacturaDetalle(self):
        return self.factura_detalle_controller
    def getRoutesSqlServer(self):
        return self.facturacion_routes,self.vendedor_routes
    def getRoutesOracle(self):
        return self.producto_routes,self.factura_detalle_routes
   
    def services_sql_server(self,db,models):
        self.facturacion_services=F_S(db,models)
        self.vendedor_services=V_S(db,models)
    def services_oracle(self,db,models):
        self.producto=P_S(db,models)
        self.factura_detalle=FD_S(db,models)
    def controllers_sql_server(self):
        self.facturacion_controller=F_C(self.facturacion_services)
        self.vendedor_controller=V_C(self.vendedor_services)
    def controllers_oracle(self):
        self.producto_controller=P_C(self.producto)
        self.factura_detalle_controller=FD_C(self.factura_detalle)
    def routes_sql_server(self):
        self.facturacion_routes=F_R(self.app,self)
        self.vendedor_routes=V_R(self.app,self)
    def routes_oracle(self):
        self.producto_routes=P_R(self.app,self)
        self.factura_detalle_routes=FD_R(self.app,self)
