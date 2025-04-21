from flask import request
class ProductoRoutes:
    def __init__(self,app,app_initializer):
        self.app_initializer=app_initializer
        self.app=app
        self.routes()
    def routes(self):
        @self.app.route('/microservice/v1/get/producto', methods=['GET'])
        def get_productos():
            return self.app_initializer.getControllersProducto().get_productos()
        @self.app.route('/microservice/v1/get/producto/<int:id>', methods=['GET'])
        def get_producto_by_id(id):
            return self.app_initializer.getControllersProducto().get_producto(id)
        @self.app.route('/microservice/v1/post/producto',methods=['POST'])
        def post_producto():
            return self.app_initializer.getControllersProducto().post_producto(request.json)
        @self.app.route('/microservice/v1/put/producto/<int:id>',methods=['PUT'])
        def put_producto(id):
            return self.app_initializer.getControllersProducto().put_producto(id,data=request.json)