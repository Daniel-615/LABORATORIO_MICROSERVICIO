from flask import request
class VendedorRoutes:
    def __init__(self,app,app_initializer):
        self.app=app
        self.app_initializer=app_initializer
        self.routes()
    def routes(self):
        @self.app.route('/v1/vendedor',methods=['POST'])
        def create_vendedor():
            return self.app_initializer.getControllersVendedor().post_vendedor(data=request.json)
        @self.app.route('/v1/vendedor',methods=['GET'])
        def get_vendedor():
            return self.app_initializer.getControllersVendedor().get_vendedores()
        @self.app.route('/v1/vendedor/<int:id>',methods=['GET'])
        def get_vendedor_by_id(id):
            return self.app_initializer.getControllersVendedor().get_vendedor(id)
        @self.app.route('/v1/vendedor/<int:id>',methods=['PUT'])
        def update_vendedor(id):
            return self.app_initializer.getControllersVendedor().put_vendedor(id,data=request.json)