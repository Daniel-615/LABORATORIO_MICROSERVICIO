import requests

class CertificadoFacturaServices:
    def __init__(self, db, models):
        self.db = db
        self.models = models

    def getDb(self):
        return self.db

    def validate_inputs(self, cae, certificado):
        if not cae or not certificado:
            return {
                "message": "Todos los campos (cae, factura, certificado) son obligatorios."
            }, 400
        return None

    def verify_cae_remotely(self, cae):
        url = f"http://127.0.0.1:5000/microservice/v1/get/facturacion/{cae}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json(), True
            else:
                return {"message": f"El CAE '{cae}' no existe en el microservicio de facturación."}, False
        except requests.exceptions.RequestException as e:
            return {"message": f"Error al conectar con el microservicio de facturación: {str(e)}"}, False

    def create_model_instance(self, cae, factura, certificado):
        return self.models.CERTIFICADO_FACTURA(
            cae=cae,
            certificado=certificado,
            factura=factura
        )

    def save_to_db(self, instance):
        db_session = self.getDb()
        if not db_session:
            return {
                "message": "Error: No se pudo obtener la sesión de base de datos."
            }, 500
        try:
            db_session.session.add(instance)
            db_session.session.commit()
            return {
                "message": "Certificado creado exitosamente.",
                "id": instance.id
            }, 201
        except Exception as e:
            db_session.session.rollback()
            return {
                "message": f"Error inesperado: {e}"
            }, 400

    def create_certificado(self, cae, factura, certificado):
        validation_error = self.validate_inputs(cae, factura, certificado)
        if validation_error:
            return validation_error

        cae_data, valido = self.verify_cae_remotely(cae)
        if not valido:
            return cae_data, 404

        new_instance = self.create_model_instance(cae, factura, certificado)
        return self.save_to_db(new_instance)

    def get_all_certificados(self, page, per_page):
        certificados = self.models.CERTIFICADO_FACTURA.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        if not certificados.items:
            return {
                "message": "No hay certificados registrados."
            }, 404

        return {
            "certificados": [self.serialize(cert) for cert in certificados.items],
            "total": certificados.total,
            "pagina_actual": certificados.page,
            "total_paginas": certificados.pages
        }, 200

    def get_certificado_by_id(self, id):
        db_session = self.getDb()
        if not db_session:
            return {
                "message": "Error: No se pudo obtener la sesión de base de datos."
            }, 500

        certificado = db_session.session.query(self.models.CERTIFICADO_FACTURA).filter_by(id=id).first()
        if not certificado:
            return {
                "message": "Certificado no encontrado por el id requerido."
            }, 404

        return {
            "certificado": self.serialize(certificado)
        }, 200

    def update_certificado(self, id, cae):
        # Verificar que exista el certificado a actualizar
        certificado = self.models.CERTIFICADO_FACTURA.query.filter_by(id=id).first()
        if not certificado:
            return {
                "message": f"No se ha encontrado el certificado con el id {id}"
            }, 404

        # Obtener datos del microservicio de facturación
        cae_data, valido = self.verify_cae_remotely(cae)
        if not valido:
            return cae_data, 404

        # Reconstruir la factura desde la respuesta del microservicio
        factura = (
            f"Factura del cliente {cae_data.get('nit_clte')} con vendedor {cae_data.get('id_vendedor')} "
            f"certificada el {cae_data.get('fecha_hora_certificado')}"
        )

        try:
            certificado.factura = factura
            certificado.cae = cae  # (opcional) por si también querés actualizar el CAE
            self.getDb().session.commit()
            return {
                "message": "Certificado actualizado correctamente."
            }, 200
        except Exception as e:
            self.getDb().session.rollback()
            return {
                "message": f"Error en el servidor: {str(e)}"
            }, 500

    def serialize(self, cert):
        return {
            "id": cert.id,
            "cae": cert.cae,
            "certificado": cert.certificado,
            "factura": cert.factura
        }