from flask import jsonify
class VendedorController:
    def __init__(self,vendedor_services):
        self.vendedor_services = vendedor_services
    def post_vendedor(self,data):
        try:
            nombre=data.get('nombre')
            if not nombre:
                return jsonify({
                    'error': "Missing required field 'nombre'"
                })
            result, status = self.vendedor_services.post_vendedor(nombre)
            return jsonify(result), status
        except Exception as e:
            print("Error in post_vendedor:", e)
            return jsonify({"error": "Ocurrió un error al crear el vendedor"}), 500
    def get_vendedores(self):
        try:
            return self.vendedor_services.get_vendedores()
        except Exception as e:
            print("Error in get_vendedores:", e)
            return jsonify({"error": "Ocurrió un error al obtener el vendedor"}), 500
    def get_vendedor(self, id):
        try:
            return self.vendedor_services.get_vendedor(id)
        except Exception as e:
            print("Error in get_vendedor:", e)
            return jsonify({"error": "Ocurrió un error al obtener el vendedor"}), 500
    def put_vendedor(self, id, data):
        try:
            nombre=data.get('nombre')
            if not nombre:
                return jsonify({
                    'error': "Missing required field 'nombre'"
                })
            return self.vendedor_services.put_vendedor(id, nombre)
        except Exception as e: 
            print("Error in put_vendedor:", e)
            return jsonify({"error": "Ocurrió un error al actualizar el vendedor"}), 500