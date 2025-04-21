from flask import jsonify

class FacturaDetalleController:
    def __init__(self, factura_detalle_services):
        self.factura_detalle_services = factura_detalle_services

    def post_factura_detalle(self, data):
        try:
            cae = data.get('cae')
            id_producto = data.get('id_producto')
            cantidad = data.get('cantidad')
            precio = data.get('precio')
            descuento = data.get('descuento')

            # Validar campos requeridos
            if not all([cae, id_producto, cantidad, precio, descuento]):
                return jsonify({
                    'error': "Faltan campos requeridos: 'cae', 'id_producto', 'cantidad', 'precio', 'descuento'"
                }), 400

            result, status = self.factura_detalle_services.post_factura_detalle(
                id_producto, cantidad, precio, descuento, cae
            )
            return jsonify(result), status

        except Exception as e:
            print("Error en post_factura_detalle:", e)
        return jsonify({"error": "Error inesperado en el servidor"}), 500

    def get_facturas_detalle(self):
        try:
            result, status = self.factura_detalle_services.get_factura_detalles()
            return jsonify(result), status
        except Exception as e:
            print("Error en get_facturas_detalle:", e)
            return jsonify({"error": "Error al obtener los detalles de facturación"}), 500

    def get_factura_detalle(self, id):
        try:
            result, status = self.factura_detalle_services.get_factura_detalle(id)
            return jsonify(result), status
        except Exception as e:
            print("Error en get_factura_detalle:", e)
            return jsonify({"error": "Error al obtener el detalle de la factura"}), 500

    def put_factura_detalle(self, id, data):
        try:
            cantidad = data.get('cantidad')
            if cantidad is None:
                return jsonify({
                    'error': "Falta el campo requerido: 'cantidad'"
                }), 400

            result, status = self.factura_detalle_services.put_factura_detalle(id, cantidad)
            return jsonify(result), status

        except Exception as e:
            print("Error en put_factura_detalle:", e)
            return jsonify({"error": "Error al actualizar el detalle de la factura"}), 500
