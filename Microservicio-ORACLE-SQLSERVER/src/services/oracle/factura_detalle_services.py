class FacturaDetalleServices:
    def __init__(self, db, models):
        self.db = db
        self.models = models

    def getDb(self):
        return self.db

    def post_factura_detalle(self, id_producto, cantidad, precio, descuento, cae):
        db = self.getDb()
        models = self.models

        try:
            # Validar existencia del producto
            producto = db.session.query(models.PRODUCTO).filter_by(id=id_producto).first()
            if not producto:
                return {"error": f"Producto con id {id_producto} no existe."}, 404

            # Validar existencia del CAE en FACTURACION
            facturacion = db.session.query(models.FACTURACION).filter_by(cae=cae).first()
            if not facturacion:
                return {"error": f"CAE '{cae}' no existe en la tabla FACTURACION."}, 404

            # Crear nuevo detalle
            nuevo_detalle = models.FACTURA_DETALLE(
                cae=cae,
                id_producto=id_producto,
                cantidad=cantidad,
                precio=precio,
                descuento=descuento
            )

            db.session.add(nuevo_detalle)
            db.session.commit()

            return {"message": "Factura detalle creada correctamente.", "id": nuevo_detalle.id}, 201

        except Exception as e:
            db.session.rollback()
            return {"error": f"Ocurrió un error al insertar: {str(e)}"}, 500

    def get_factura_detalles(self):
        db = self.getDb()
        models = self.models

        try:
            detalles = db.session.query(models.FACTURA_DETALLE).all()
            return [detalle.to_dict() for detalle in detalles], 200

        except Exception as e:
            print("Error en get_factura_detalles:", e)
            return {"error": "Ocurrió un error al obtener los detalles de la factura"}, 500

    def get_factura_detalle(self, id):
        db = self.getDb()
        models = self.models

        try:
            detalle = db.session.query(models.FACTURA_DETALLE).filter_by(id=id).first()

            if not detalle:
                return {"error": f"Factura detalle con id {id} no encontrado."}, 404

            return detalle.to_dict(), 200

        except Exception as e:
            print("Error en get_factura_detalle:", e)
            return {"error": "Ocurrió un error al obtener el detalle de la factura"}, 500

    def put_factura_detalle(self, id, cantidad):
        db = self.getDb()
        models = self.models

        try:
            detalle = db.session.query(models.FACTURA_DETALLE).filter_by(id=id).first()

            if not detalle:
                return {"error": f"Factura detalle con id {id} no encontrado."}, 404

            detalle.cantidad = cantidad
            db.session.commit()

            return {"message": "Factura detalle actualizado correctamente."}, 200

        except Exception as e:
            db.session.rollback()
            print("Error en put_factura_detalle:", e)
            return {"error": "Ocurrió un error al actualizar el detalle de la factura"}, 500
