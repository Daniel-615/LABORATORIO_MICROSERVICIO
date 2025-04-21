from flask import request
class FacturacionRoutes:
    def __init__(self,app,app_initializer):
        self.app=app
        self.app_initializer=app_initializer
        self.routes()  
    def routes(self):
        @self.app.route('/microservice/v1/post/facturacion',methods=['POST'])
        def create_factura():
            return self.app_initializer.getControllersFacturacion().post_factura(data=request.json)
        @self.app.route('/microservice/v1/get/facturacion',methods=['GET'])
        def get_factura():
            return self.app_initializer.getControllersFacturacion().get_facturas()
        @self.app.route('/microservice/v1/get/facturacion/<string:cae>',methods=['GET'])
        def get_factura_by_id(cae):
            return self.app_initializer.getControllersFacturacion().get_factura(cae)
        @self.app.route('/microservice/v1/put/facturacion/<string:cae>',methods=['PUT'])
        def update_factura(cae):
            return self.app_initializer.getControllersFacturacion().put_factura(cae,data=request.json)