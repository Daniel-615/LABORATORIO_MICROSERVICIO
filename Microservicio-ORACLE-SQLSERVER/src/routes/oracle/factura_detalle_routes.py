from flask import request
class FacturaDetalleRoutes:
    def __init__(self,app,app_initializer):
        self.app=app
        self.app_initializer=app_initializer
        self.routes()
    def routes(self):
        @self.app.route('/v1/factura_detalle', methods=['GET'])
        def get_facturas_detalle():
            return self.app_initializer.getControllersFacturaDetalle().get_facturas_detalle()
        @self.app.route('/v1/factura_detalle/<int:id>', methods=['GET'])
        def get_factura_detalle_by_id(id):
            return self.app_initializer.getControllersFacturaDetalle().get_factura_detalle(id)
        @self.app.route('/v1/post/factura_detalle',methods=['POST'])
        def post_factura_detalle():
            return self.app_initializer.getControllersFacturaDetalle().post_factura_detalle(request.json)
        @self.app.route('/v1/put/factura_detalle/<int:id>',methods=['PUT'])
        def put_factura_detalle(id):
            return self.app_initializer.getControllersFacturaDetalle().put_factura_detalle(id,data=request.json)
        