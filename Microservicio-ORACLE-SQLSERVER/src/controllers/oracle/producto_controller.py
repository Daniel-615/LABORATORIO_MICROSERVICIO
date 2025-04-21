from flask import jsonify
class ProductoController:
    def __init__(self, producto_services):
        self.producto_services = producto_services
    def post_producto(self, data):
        try:
            nombre=data.get('nombre')
            stock=data.get('stock')
            if not nombre or not stock:
                return jsonify({
                    'error': "Missing required fields 'precio','stock'"
                })
            return self.producto_services.post_producto(nombre,stock)
        except Exception as e:
            print("Error in post_producto:", e)
    def get_productos(self):
        try:
            return self.producto_services.get_productos()
        except Exception as e:
            print("Error in get_productos:", e)
    def get_producto(self, id):
        try:
            return self.producto_services.get_producto(id)
        except Exception as e:
            print("Error in get_producto:", e)
    def put_producto(self, id, data):
        try:
            stock=data.get('stock')
            if not stock:
                return jsonify({
                    'error': "Missing required fields 'precio','stock'"
                })
            return self.producto_services.put_producto(id,stock)
        except Exception as e: 
            print("Error in put_producto:", e)
            