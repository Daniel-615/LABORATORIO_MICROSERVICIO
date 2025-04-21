from flask import jsonify

class FacturacionController:
    def __init__(self, facturacion_services):
        self.facturacion_services = facturacion_services

    def post_factura(self, data):
        try:
            cae = data.get('cae')
            nit_clte = data.get('nit_clte')
            fecha_hora_certificado = data.get('fecha_hora_certificado')
            fecha_hora_validacion = data.get('fecha_hora_validacion')
            id_vendedor = data.get('id_vendedor')

            # Validación de campos requeridos
            if not all([cae, nit_clte, fecha_hora_certificado, fecha_hora_validacion, id_vendedor]):
                return jsonify({
                    'error': "Faltan campos requeridos: 'cae', 'nit_clte', 'fecha_hora_certificado', 'fecha_hora_validacion', 'id_vendedor'"
                }), 400

            result, status = self.facturacion_services.post_factura(
                cae, nit_clte, fecha_hora_certificado, fecha_hora_validacion, id_vendedor
            )
            return jsonify(result), status

        except Exception as e:
            print("Error en post_factura:", e)
            return jsonify({"error": "Error inesperado al crear la factura"}), 500

    def get_facturas(self):
        try:
            result, status = self.facturacion_services.get_facturas()
            return jsonify(result), status
        except Exception as e:
            print("Error en get_facturas:", e)
            return jsonify({"error": "Error inesperado al obtener las facturas"}), 500

    def get_factura(self, cae):
        try:
            result, status = self.facturacion_services.get_factura(cae)
            return jsonify(result), status
        except Exception as e:
            print("Error en get_factura:", e)
            return jsonify({"error": "Error inesperado al obtener la factura"}), 500

    def put_factura(self, cae, data):
        try:
            fecha_hora_validacion = data.get('fecha_hora_validacion')
            if not fecha_hora_validacion:
                return jsonify({
                    'error': "Falta el campo requerido: 'fecha_hora_validacion'"
                }), 400

            result, status = self.facturacion_services.put_factura(cae, fecha_hora_validacion)
            return jsonify(result), status

        except Exception as e:
            print("Error en put_factura:", e)
            return jsonify({"error": "Error inesperado al actualizar la factura"}), 500
