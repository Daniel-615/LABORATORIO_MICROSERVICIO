from flask import jsonify,request
class CertificadoFacturaControllers:
    def __init__(self, service):
        self.service = service

    def post_certificado(self, data):
        if not data:
            return jsonify({
                'message': 'Debes colocar contenido en el body formato json.'
            }),404
        try:
            cae=data.get('cae')
            certificado=data.get('certificado')
            result = self.service.create_certificado(cae,certificado)
            return jsonify(result), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_certificados(self):
        page = request.args.get('page',default=1,type=int)
        per_page = request.args.get('per_page',default=10,type=int)  # Número de elementos por página por defecto
        try:
            result = self.service.get_all_certificados(page,per_page)
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_certificado_id(self, id):
        if not id:
            return jsonify({
                'message': 'Debes incluir el id en la ruta.'
            }),400
        try:
            result = self.service.get_certificado_by_id(id)
            if result:
                return jsonify(result), 200
            return jsonify({"error": "Certificado no encontrado"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def put_certificado(self, id, data):
        if not id:
            return jsonify({
                'message': 'Debes incluir el id en la ruta.'
            }),400
        if not data:
            return jsonify({
                'message': 'Debes colocar contenido en el body formato json.'
            }),404
        try:
            cae=data.get('cae')
            if not cae:
                return jsonify({
                    "'factura' es obligatorio."
                }),400
            result = self.service.update_certificado(id, cae)
            if result:
                return jsonify(result), 200
            return jsonify({"error": "Certificado no encontrado"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
