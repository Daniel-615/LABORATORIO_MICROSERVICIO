class FacturacionServices:
    def __init__(self, db, models):
        self.models = models
        self.db = db

    def getDb(self):
        return self.db

    def post_factura(self, cae, nit_clte, fecha_hora_certificado, fecha_hora_validacion, id_vendedor):
        db = self.getDb()
        models = self.models

        try:
            # Verificar si ya existe una factura con el mismo CAE
            factura_existente = db.session.query(models.FACTURACION).filter_by(cae=cae).first()
            if factura_existente:
                return {"error": f"Ya existe una factura con el CAE '{cae}'."}, 400

            # Verificar si el vendedor existe
            vendedor = db.session.query(models.VENDEDOR).filter_by(id=id_vendedor).first()
            if not vendedor:
                return {"error": f"Vendedor con id {id_vendedor} no existe."}, 404

            # Crear nueva instancia de FACTURACION
            nueva_factura = models.FACTURACION(
                cae=cae,
                nit_clte=nit_clte,
                fecha_hora_certificado=fecha_hora_certificado,
                fecha_hora_validacion=fecha_hora_validacion,
                id_vendedor=id_vendedor
            )

            db.session.add(nueva_factura)
            db.session.commit()

            return {"message": "Factura creada correctamente.", "cae": nueva_factura.cae}, 201

        except Exception as e:
            db.session.rollback()
            print("Error en post_factura:", e)
            return {"error": "Ocurrió un error al insertar la factura."}, 500

    def get_facturas(self):
        db = self.getDb()
        models = self.models

        try:
            facturas = db.session.query(models.FACTURACION).all()
            return [factura.to_dict() for factura in facturas], 200

        except Exception as e:
            print("Error en get_facturas:", e)
            return {"error": "Ocurrió un error al obtener las facturas."}, 500

    def get_factura(self, cae):
        db = self.getDb()
        models = self.models

        try:
            factura = db.session.query(models.FACTURACION).filter_by(cae=cae).first()

            if not factura:
                return {"error": f"Factura con CAE '{cae}' no encontrada."}, 404

            return factura.to_dict(), 200

        except Exception as e:
            print("Error en get_factura:", e)
            return {"error": "Ocurrió un error al obtener la factura."}, 500

    def put_factura(self, cae, fecha_hora_validacion):
        db = self.getDb()
        models = self.models

        try:
            factura = db.session.query(models.FACTURACION).filter_by(cae=cae).first()

            if not factura:
                return {"error": f"Factura con CAE '{cae}' no encontrada."}, 404

            factura.fecha_hora_validacion = fecha_hora_validacion
            db.session.commit()

            return {"message": "Factura actualizada correctamente."}, 200

        except Exception as e:
            db.session.rollback()
            print("Error en put_factura:", e)
            return {"error": "Ocurrió un error al actualizar la factura."}, 500